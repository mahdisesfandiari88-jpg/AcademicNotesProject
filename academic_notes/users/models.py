from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    GENDERS = [
        ("female", "Female"),
        ("male", "Male"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDERS,
        blank=True,
    )

    major = models.CharField(
        max_length=100,
        blank=True
    )

    university = models.CharField(
        max_length=150,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username