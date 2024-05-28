from django.urls import path

from hardrada.core import views


urlpatterns = [
    path('<action>/', views.hardrada_actions, name='hardrada.actions'),
]