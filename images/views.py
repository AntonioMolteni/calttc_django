from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.forms import modelformset_factory
from django import forms

from .forms import CarouselImageForm
from .models import CarouselImage
from .forms import FooterImageForm
from .models import FooterImage
 
@staff_member_required
def edit_carousel_images(request):
    page_title = 'Edit Carousel Images'
    widgets = {  
                "image": forms.ClearableFileInput(attrs={'class':'form-control-file','style':'margin-top:0.5rem; font-size:1rem;'}),
                "name": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name','style':'margin-top:0.5rem;'}),
    }
    all_carousel_images = CarouselImage.objects.all().order_by("name")
    initial = [{
        'image': None,
        'name': None,
        }]

    CarouselImagesFormSet = modelformset_factory(CarouselImage, form=CarouselImageForm, widgets=widgets, extra=0,)
    if request.method == "POST":
        formset = CarouselImagesFormSet(request.POST, request.FILES, queryset=all_carousel_images, initial=initial,
        )
        if formset.is_valid():
            formset.save()
            return redirect(reverse('edit-carousel-images'))
    else:
        formset = CarouselImagesFormSet(queryset=all_carousel_images, initial=initial)
        
    return render(request, 'images/edit_carousel_images.html',
        {
            'page_title': page_title,
            'formset':formset,
        })

@staff_member_required
def edit_footer_images(request):
    page_title = 'Edit Footer Images'
    widgets = {  
                "image": forms.ClearableFileInput(attrs={'class':'form-control-file','style':'margin-top:0.5rem; font-size:1rem;'}),
                "name": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name','style':'margin-top:0.5rem;'}),
    }
    all_footer_images = FooterImage.objects.all()
    initial = [{
        'image': None,
        'name': None,
        }]

    FooterImagesFormSet = modelformset_factory(FooterImage, form=FooterImageForm, widgets=widgets, extra=1,)
    if request.method == "POST":
        formset = FooterImagesFormSet(request.POST, request.FILES, queryset=all_footer_images, initial=initial,
        )
        if formset.is_valid():
            formset.save()
            return redirect(reverse('edit-footer-images'))
    else:
        formset = FooterImagesFormSet(queryset=all_footer_images, initial=initial)
        
    return render(request, 'images/edit_footer_images.html',
        {
            'page_title': page_title,
            'formset': formset,
        })