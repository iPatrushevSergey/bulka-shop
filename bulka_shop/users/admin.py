from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel of the user model.
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'username')
