"""Django admin customization"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):

    """Define admin pages for users."""
    ordering = ['id']
    list_display = ['email','name']
    fieldsets =(
        (
            None,{'fields':('email','password')}
        ),(_('Personal Info'), {'fields':('name',)}),
        (
            _('Permissions'),{
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (_('Important Dates'),{'fields':('last_login',)})
    )
    readonly_fields =['last_login']

     # Optional: Add list_filter for better admin experience
    list_filter = ('is_active', 'is_staff', 'is_superuser')

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser'
                ),
            }
        ),
    )


admin.site.register(models.User,UserAdmin)
