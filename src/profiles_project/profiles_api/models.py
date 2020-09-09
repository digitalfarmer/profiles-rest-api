from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Help Django work with our custom our model"""

    def create_user(self, name, email, password=None):
        """Createna new user profile object"""

        if not email:
            raise ValueError("User must have email address.")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and saved a new superuser with givesn detail"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a UserProfile inside our system"""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField( max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['name']

    def get_full_name(self):
        """Used to get a users full name"""

        return self.name

    def get_sort_name(self):
        """Used to get a users sort name"""
        return self.name

    def __str__(self):
        """Django use this when it needs to convert the object to a string"""
        return self.email
    
