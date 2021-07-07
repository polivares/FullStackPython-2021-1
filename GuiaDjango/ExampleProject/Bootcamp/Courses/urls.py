from django.urls import path
from Courses import views

urlpatterns = [
    path('',views.index),
    path('student/', views.student),
]