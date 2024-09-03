from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_workout),
    path('stretch/', views.stretch_view, name='stretch'),
    path('strength/', views.strength_view, name='strength'),
    path('cardio/', views.cardio_view, name='cardio')
]