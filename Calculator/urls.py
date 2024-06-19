from django.urls import path
from .views import SIPCalculator

urlpatterns = [
    path('calculate_sip/', SIPCalculator.as_view(), name='calculate_sip')
]