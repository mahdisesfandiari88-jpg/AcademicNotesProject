from django.db import models
from courses.models import Course

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title