from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email!")
        user = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            self.normalize_email(email),
            password=password,
        ) 
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin): 
    id = models.BigAutoField(primary_key=True, serialize=False)
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email