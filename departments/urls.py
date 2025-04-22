from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('create/', views.create_department, name='create_department'),
    path('departments/edit/<int:pk>/', views.edit_department, name='edit_department'),
    path('delete/<int:pk>/', views.delete_department, name='delete_department'),
    path('departments/', views.dashboard, name="dashboard")
]
