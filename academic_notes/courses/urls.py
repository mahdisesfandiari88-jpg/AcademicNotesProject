from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path("create/", views.course_create, name="add_course"),
    path('<int:id>/', views.course_detail, name='course_detail'),
    path('<int:id>/edit/', views.course_update, name='course_update'),
    path('<int:id>/delete/', views.course_delete, name='course_delete'),
]