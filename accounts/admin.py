from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountChangeForm
from .models import User


class AccountUserAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_member', 'rating', 'is_admin', 'is_staff', 'is_active', 'date_joined', 'last_login', 'has_berkeley_email',)
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name','rating', 'is_member',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'groups')}),
    )
    readonly_fields=('email','groups',)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super().get_readonly_fields(request, obj))
        if not request.user.is_superuser:
            readonly_fields.append('is_admin')
            if not request.user.is_admin:
                readonly_fields.append('is_staff')
        return readonly_fields
    
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