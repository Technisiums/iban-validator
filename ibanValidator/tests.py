from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status


class IbanValidator(APITestCase):
    def test_montenegro_iban_valid_scenarios(self):
        """
        Tests by sending a valid IBAN to the endpoint
        """
        self.api_client = APIClient()
        response = self.api_client.get(reverse('iban-validation') + '?iban=ME59234342312345654213')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_valid'], True)

    def test_montenegro_iban_invalid_scenarios(self):
        """
            Tests by sending an in-valid IBAN to the endpoint
        """
        self.api_client = APIClient()
        response = self.api_client.get(reverse('iban-validation') + '?iban=ME59234342319845654217')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['is_valid'], False)
