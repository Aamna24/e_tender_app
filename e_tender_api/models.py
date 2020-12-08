from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, organization_name, email, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not organization_name:
            raise ValueError('Organization Name is no correct')

        email=self.normalize_email(email)
        user = self.model(organization_name=organization_name,email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, organization_name, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        user=self.create_user(organization_name,email,password,**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    organization_name = models.CharField(max_length=255)
    #password=models.CharField(max_length=250,default='')      
    ntn=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    contact=PhoneNumberField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['organization_name']

    def get_full_name(self):
        """Retrieve full name of users"""
        return self.organization_name

    def get_short_name(self):
        """Retrieve short name of users"""
        return self.organization_name

    def __str__(self):
        """Return string representation of user"""
        return self.email

