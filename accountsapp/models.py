from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')



    def save(self, *args, **kwargs):

        if self.is_superuser:
            self.role = "admin"

        if self.role == "admin" and CustomUser.objects.filter(role="admin").exclude(id=self.id).exists():
            raise ValidationError("Only one admin is allowed in the system.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username