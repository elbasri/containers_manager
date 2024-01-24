from django.urls import path
from . import views

urlpatterns = [
    path('', views.container_list, name='container_list'),
    path('update/<int:container_id>/', views.update_container_status, name='update_container_status'),
]
