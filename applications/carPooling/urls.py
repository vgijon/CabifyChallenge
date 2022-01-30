from django.urls import path
from . import views


urlpatterns = [
    path('status/', views.StatusView.as_view()),
    path('cars/', views.LoadCarsView.as_view()),
]
