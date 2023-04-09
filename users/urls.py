from . import views
from django.urls import path

urlpatterns = [
    path('authorization/', views.authorization_api_view),
    path('registration/', views.registration_api_view),
    path('confirm/', views.confirmation_api_view),
]