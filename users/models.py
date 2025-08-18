from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES=(
        ('donor', 'Donor'),
        ('superadmin','SuperAdmin'),
        ('ngoadmin','NGO Admin'),
        ('volunteer','Volunteer'),
    )
    role=models.CharField(max_length=20, choices=ROLE_CHOICES, default='donor')
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username 
    
