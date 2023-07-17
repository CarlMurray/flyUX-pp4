from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        '''
        Creates and saves a User with the given email, first/last name and password.
        '''
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None):
        '''
        Creates and saves a Superuser with the given email, first/last name and password.
        '''
        if not email:
            raise ValueError("Superusers must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    '''
    Defines User model
    '''
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = UserManager()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

