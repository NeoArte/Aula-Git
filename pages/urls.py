from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    
    path('details/<int:pk>/', views.details, name="details"),
    path('form/', views.form, name="form"),
    path('create/', views.create),
    path('edit/<int:pk>/', views.edit, name="edit"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),

    path('sobre/', views.sobre, name="sobre"),
    path('servicos/', views.servicos, name="servicos"),
    path('contatos/', views.contatos, name="contatos"),
]