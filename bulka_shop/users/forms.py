from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Expands the user creation form to be able to work with a custom
    user model.
    """

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """
    Expands the user editing form to be able to work with a custom user model.
    """

    class Meta:
        model = User
        fields = ('username', 'email')
