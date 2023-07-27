from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class IBANValidation(APIView):
    def get(self, request):
        """
        endpoint to validate Montenegro's IBANs
        :param request: containing IBAN as a query param
        :return: {'is_valid':bool}
        """
        iban = request.GET.get('iban', '')

        return Response({'is_valid': validate_montenegro_iban(iban)}, status=status.HTTP_200_OK)


def validate_montenegro_iban(iban: str) -> bool:
    """
    normalize and validates Montenegro's IBAN based on following criteria
        - IBAN length == 22 characters
        - Must start with ME and remaining string must be numeric
        - Move first 4 characters to the end
        - Covert ME to numbers, i.e M=22, E=14 -> 2214
        - take the mode of the resultant integer with 97
        - If the answer is 1, IBAN is correct else not

    :param iban: IBAN as a string
    :return: true if correct else false
    """
    iban = iban.replace(" ", '').upper()

    if len(iban) != 22 or iban[:2] != 'ME' or not iban[2:].isnumeric():
        return False

    iban = iban[4:] + iban[:4]
    iban = iban.replace('ME', '2214')
    remainder = int(iban) % 97
    return remainder == 1
