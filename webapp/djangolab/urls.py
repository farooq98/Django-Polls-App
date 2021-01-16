from django.urls import path
from .views import show, about

urlpatterns = [
    path('', show),
    path('about/', about),
]
