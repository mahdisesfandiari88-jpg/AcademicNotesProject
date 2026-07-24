from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    COLORS = [
        ("green", "Green"),
        ("pink", "Pink"),
        ("orange", "Orange"),
        ("purple", "Purple"),
    ]

    name = models.CharField(max_length=100)

    description = models.TextField(
        blank=True
    )

    color = models.CharField(
        max_length=20,
        choices=COLORS,
        default="green"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name