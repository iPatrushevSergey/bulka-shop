from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom user model, initializes user objects.
    """

    email = models.EmailField(
        _('Email'),
        help_text=_('Required field, no more than 150 characters.'),
        db_index=True,
        max_length=150,
        unique=True,
    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        """
        Returns the user name.
        """
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
