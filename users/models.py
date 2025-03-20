from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        user = self.model(
            username=username, 
            email=email, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('admin', True)

        return self.create_user(username, email, password, **extra_fields)
    

# Create your models here.
class UserModel(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    names = models.CharField(max_length=200, blank=True, null=True)
    last_names = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'names', 'last_names']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin

    @is_staff.setter
    def is_staff(self, value):
        self.admin = value 
    