from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """
    Expands the user creation form to be able to work with a custom
    user model.
    """

    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """
    Expands the user editing form to be able to work with a custom user model.
    """

    class Meta:
        model = get_user_model()
        fields = ('username', 'email')
