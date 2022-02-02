from django.urls import path
from . import views


urlpatterns = [
    path('status/', views.StatusView.as_view()),
    path('cars/', views.LoadCarsView.as_view()),
    path('journey/', views.BookingJourneyView.as_view()),
    path('dropoff/', views.DropOffJourneyView.as_view()),
    path('locale/', views.LocaleView.as_view()),
]
