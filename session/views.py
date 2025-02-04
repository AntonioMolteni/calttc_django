from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from announcements.models import Announcement
from .models import Session, cutoff
from accounts.models import User
from datetime import datetime, timedelta
from .forms import AddSessionsForm, EditSessionForm
from django.forms import modelformset_factory, TextInput


def refresh_queries():
    global all_available_sessions
    global all_sessions
    all_available_sessions = (
        Session.objects.filter(time__gte=datetime.now() + timedelta(minutes=cutoff))
        .exclude(is_closed=True)
        .exclude(is_cancelled=True)
    )
    all_sessions = Session.objects.filter(
        time__gte=datetime.now() - timedelta(hours=3)
    ).order_by("time")


# helper function to determine if user has already signed up or has been queued and returns a tuple of boolean values
def has_signed_up(request):
    already_signed_up = False
    already_queued = False
    if request.user.is_authenticated:
        # exclude tournaments so that you can still sign up for multiple sessions
        for session in all_available_sessions.exclude(session_type="RR").exclude(
            session_type="TO"
        ):
            if session.players.contains(request.user):
                already_signed_up = True
            if session.queue.contains(request.user):
                already_queued = True
    return (already_signed_up, already_queued)


def sessions(request):
    page_title = "Sessions"
    refresh_queries()
    already_signed_up, already_queued = (
        has_signed_up(request)[0],
        has_signed_up(request)[1],
    )
    # Update roster
    for session in all_sessions:
        if session.get_queue() and datetime.now() >= session.time - timedelta(
            minutes=cutoff
        ):
            extra_space = max(0, session.capacity - session.players.count())
            for user in session.queue.order_by(
                "-is_member",
                "-has_berkeley_email",
                "sign_up_date",
            )[:extra_space].all():
                user_signed_up = False
                for s in all_available_sessions:
                    if s.players.contains(user):
                        user_signed_up = True
                if not user_signed_up:
                    session.players.add(user)
                    session.queue.remove(user)
                    already_queued = False

    announcements = Announcement.objects.filter(on_sessions_page=True)

    return render(
        request,
        "sessions/sessions.html",
        {
            "page_title": page_title,
            "cutoff": cutoff,
            "all_sessions": all_sessions,
            "already_signed_up": already_signed_up,
            "already_queued": already_queued,
            "announcements": announcements,
        },
    )


@login_required
@staff_member_required
def add_sessions(request):
    if request.method == "POST":
        form = AddSessionsForm(request.POST)

        if form.is_valid():
            total_duration = form.cleaned_data["total_duration"]
            num_sessions = form.cleaned_data["num_sessions"]
            start_time = form.cleaned_data["start_time"]

            duration_per_session = total_duration // num_sessions
            session_time = start_time

            sessions = []

            for _ in range(num_sessions):
                session = Session(
                    session_type=form.cleaned_data["session_type"],
                    location=form.cleaned_data["location"],
                    time=session_time,
                    duration=duration_per_session,
                    capacity=form.cleaned_data["capacity"],
                    note=form.cleaned_data["note"],
                )
                session.save()
                session.coaches.set(form.cleaned_data["coaches"])
                sessions.append(session)

                session_time += timedelta(minutes=duration_per_session)

            return redirect(reverse("sessions") + "#" + sessions[0].get_id())
    else:
        form = AddSessionsForm()

    return render(request, "sessions/add_sessions.html", {"form": form})


@login_required
@staff_member_required
def edit_session(request, session_id):
    session = Session.objects.get(pk=session_id)
    form = EditSessionForm(request.POST or None, instance=session)
    if form.is_valid():
        form.save()
        return redirect(reverse("sessions") + "#" + session.get_id())

    return render(
        request, "sessions/edit_session.html", {"session": session, "form": form}
    )


@login_required
@staff_member_required
def delete_session(request, session_id):
    session = Session.objects.get(pk=session_id)
    session.delete()
    return redirect(reverse("sessions") + "#sign-up")


@login_required
@staff_member_required
def roster_by_rating(request, session_id):
    session = Session.objects.get(pk=session_id)
    players = session.players.order_by("-rating")
    UserFormSet = modelformset_factory(
        User,
        fields=("rating",),
        widgets={
            "rating": TextInput(
                attrs={"class": "form-control rating", "type": "tel"},
            )
        },
        extra=0,
    )
    if request.method == "POST":
        formset = UserFormSet(
            request.POST,
            request.FILES,
            queryset=players,
        )
        if formset.is_valid():
            formset.save()
            return redirect(reverse("sessions") + "#" + session.get_id())
    else:
        formset = UserFormSet(queryset=players)
    return render(
        request,
        "sessions/roster_by_rating.html",
        {
            "formset": formset,
        },
    )


@login_required
def drop(request, session_id):
    session = Session.objects.get(pk=session_id)
    session.players.remove(request.user)
    session.queue.remove(request.user)
    return redirect(reverse("sessions") + "#" + session.get_id())


@login_required
def sign_up(request, session_id):
    refresh_queries()
    already_signed_up, already_queued = (
        has_signed_up(request)[0],
        has_signed_up(request)[1],
    )

    session = Session.objects.get(pk=session_id)
    if session.is_available():
        if session.is_tournament():
            session.players.add(request.user)
        elif session.is_competitive_team_tryouts() and request.user.rating == 0:
            return redirect(reverse("sessions") + "?no_rating=True")
        elif session.is_competitive_team_tryouts():
            session.players.add(request.user)
        else:
            if not already_signed_up:
                request.user.sign_up_date = datetime.now()
                request.user.save()
                session.players.add(request.user)
            if already_signed_up and not already_queued:
                session.queue.add(request.user)
            if session.queue.contains(request.user) and session.players.contains(
                request.user
            ):
                session.queue.remove(request.user)

    return redirect(reverse("sessions") + "#" + session.get_id())
