from django.urls import path
from .views import show, about, getData, submitResponse, showResults

urlpatterns = [
    path('', show),
    path('about/', about),
    path('<int:question_id>/', getData),
    path('thankyou/', submitResponse),
    path('results/', showResults)
]
