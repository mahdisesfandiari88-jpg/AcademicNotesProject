from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list),
    path('course/<int:id>/', views.course_notes, name='course_notes'),
    path('create/', views.note_create, name='note_create'),
    path('course/<int:id>/create/', views.note_create, name='course_note_create'),
    path('<int:id>/', views.note_detail, name='note_detail'),
    path('<int:id>/edit/', views.note_update, name='note_update'),
    path('<int:id>/delete/', views.note_delete, name='note_delete'),
]