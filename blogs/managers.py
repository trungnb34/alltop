from django.db import models
from django.contrib.auth.models import (
    BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password, **fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            **fields,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user