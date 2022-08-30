from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='base'),
    path('feedback/', FeedbackApp.as_view(), name='feedback'),
    path('review/', BookReview.as_view(), name='review'),
    path('search/', SearchPerson.as_view(), name='search'),
    path('result/', SearchResult.as_view(), name='result'),
]