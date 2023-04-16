from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import CustomUserCreationForm


class SignUpView(CreateView):
    """
    User registration.
    """

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'
