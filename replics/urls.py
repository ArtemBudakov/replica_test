from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_workers, name='create_workers'),
    path('db/', views.database_main, name='database_main'),
    path('replica/', views.database_replica, name='database_replica'),
]
