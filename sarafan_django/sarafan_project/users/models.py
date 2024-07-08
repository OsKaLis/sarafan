from django.contrib.auth.models import AbstractUser
from django.db import models

from .configurations import (
    STANDARD_FIELD_VALUE, EMAIL_FIELD_VALUE
)


class Users(AbstractUser):
    """Таблица пользователей."""
    USER_TEMPLATE = '{}: {}. {}.'
    username = models.CharField(
        'Логин',
        max_length=STANDARD_FIELD_VALUE,
        unique=True,
    )
    first_name = models.CharField(
        'Имя пользователя',
        max_length=STANDARD_FIELD_VALUE,
        blank=True,
    )
    last_name = models.CharField(
        'Фамилия пользователя',
        max_length=STANDARD_FIELD_VALUE,
        blank=True,
    )
    email = models.CharField(
        'Адрес электроной почты',
        max_length=EMAIL_FIELD_VALUE,
        unique=True,
    )

    class Meta:
        ordering = ('last_name', 'first_name', 'username')
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.USER_TEMPLATE.format(
            self.username,
            self.first_name,
            self.last_name
        )
