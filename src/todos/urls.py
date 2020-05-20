from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todo_list_view, name='alltodos'),
    path('<str:slug>/edit', views.todo_update_view, name='edit'),
]