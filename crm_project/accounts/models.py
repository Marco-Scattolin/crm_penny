from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('webdev', 'Web Developer'),
        ('designer', 'UI/UX Designer'),
        ('copywriter', 'Copywriter'),
        ('social_media', 'Social Media Manager'),
        ('strategy', 'Strategia Digitale e Analisi Dati'),
        ('admin', 'Amministratore'),
        ('dev', 'Sviluppo'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='webdev')
