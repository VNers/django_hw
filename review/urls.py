from django.urls import path
from . import views

urlpatterns = [
    path('submit-review/', views.submit_review, name='submit_review'),
    path('thank-you/', views.thank_you, name='thank_you'),
]