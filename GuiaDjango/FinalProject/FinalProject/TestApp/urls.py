from django.urls import path
from TestApp import views

urlpatterns = [
    path('', views.index),
    path('signin/', views.signin),
    path('register/', views.register),
    path('dashboard/admin/', views.dashboard_admin),
    path('users/new/', views.users_new),
    path('users/show/<int:user_id>/', views.show_user),
    path('users/edit/<int:user_id>/', views.edit_user),
    path('dashboard/', views.dashboard),
    path('users/edit/', views.users_edit)
]