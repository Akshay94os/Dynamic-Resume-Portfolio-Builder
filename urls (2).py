from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_resume, name='create_resume'),
    path('preview/<int:pk>/', views.preview_resume, name='preview_resume'),
]
