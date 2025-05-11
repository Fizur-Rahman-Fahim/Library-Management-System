from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string

def generate_unique_library_card():
    while True:
        card_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if not UserProfile.objects.filter(library_card_number=card_number).exists():
            return card_number

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    library_card_number = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.user.username