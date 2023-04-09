from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Extends the form to work with the users custom model.
    """

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """
    Extends the form to work with the users custom model.
    """

    class Meta:
        model = User
        fields = ('username', 'email')
