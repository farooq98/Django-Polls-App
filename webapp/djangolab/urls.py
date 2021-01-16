from django.urls import path
from .views import show, about, getData

urlpatterns = [
    path('', show),
    path('about/', about),
    path('<int:question_id>/', getData),
]
