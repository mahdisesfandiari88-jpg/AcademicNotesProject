from django.urls import path
from . import views

urlpatterns = [
    path(
        "course/<int:id>/",
        views.course_files,
        name="course_files",
    ),
    path(
    "course/<int:id>/create/",
    views.file_create,
    name="file_create",
    ),
    path(
    "<int:id>/delete/",
    views.file_delete,
    name="file_delete",
    ),
]