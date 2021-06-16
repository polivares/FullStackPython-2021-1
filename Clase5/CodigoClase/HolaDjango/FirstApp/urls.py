from django.urls import path
from FirstApp import views

urlpatterns = [
    path('nuevaApp/', views.newApp),
]