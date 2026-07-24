from django.db import models
from courses.models import Course


class File(models.Model):
    title = models.CharField(
        max_length=100
    )

    file = models.FileField(
        upload_to="course_files/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.title