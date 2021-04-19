from django.db import models
# from django.db.models import F
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)



class UserManager(BaseUserManager):
    """
    base manager class for User model, use as User.objects
    """
    def _create_user(self, email, **extra_fields):
        if not email:
            raise ValueError("the given phone number must be set")
        
        user = self.model(email=email, **extra_fields)
        user.set_password(extra_fields.get("password"))
        user.save(using=self._db)
        return user

    def create_user(self, email, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, **extra_fields)

    def create_superuser(self, email, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, **extra_fields)


class User(AbstractBaseUser):
    """
    User model 
    """
    email = models.EmailField(blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # def __str__(self):
    #     return f"{self.phone_number} {self.name} {self.family} {self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

