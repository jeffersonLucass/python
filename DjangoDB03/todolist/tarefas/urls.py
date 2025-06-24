from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_tarefa, name='add_tarefa'),
    path('delete/<int:id>/', views.delete_tarefa, name='delete_tarefa'),
    path('edit/<int:id>/', views.edit_tarefa, name='edit_tarefa'),
]
