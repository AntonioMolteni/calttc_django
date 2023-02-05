from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountChangeForm
from .models import User


class AccountUserAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_member', 'rating','is_staff', 'is_registered', 'is_checked_in', 'paid_drop_in_fee', 'last_drop_in_date', 'newsletter_subscription', 'has_berkeley_email', 'is_admin', 'date_joined', 'is_active',)
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name','rating', 'is_checked_in', 'paid_drop_in_fee', 'is_registered', 'is_member', 'newsletter_subscription','last_drop_in_date')}),
        ('Permissions', {'fields': ('is_staff','is_admin', 'is_active', 'groups')}),
    )
    readonly_fields=('email','is_staff','is_admin',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_staff', 'is_active',)}
        ),
    )
    search_fields = ('email','first_name','last_name',)
    list_per_page = 50
    ordering = ('-date_joined',)

    def get_form(self, request, obj, **kwargs):
        if obj.groups.filter(name="Admin").exists():
            obj.is_admin = True
        else:
            obj.is_admin = False

        if obj.groups.filter(name="Staff").exists():
            obj.is_staff = True
        else:
            obj.is_staff = False
        return super().get_form(request, obj, **kwargs)

    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(User, AccountUserAdmin)