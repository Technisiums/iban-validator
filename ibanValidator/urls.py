from django.urls import path
from .views import IBANValidation

urlpatterns = [
    path('validate_iban/', IBANValidation.as_view(), name='iban-validation'),
]