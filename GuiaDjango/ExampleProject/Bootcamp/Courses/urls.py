from django.urls import path
from Courses import views

urlpatterns = [
    path('',views.index),
    path('student/', views.student),
    path('professor/', views.professor),
    path('create_course/', views.create_course),
]