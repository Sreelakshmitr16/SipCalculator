from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SIPInputSerializer

class SIPCalculator(APIView):
    def post(self, request):
        serializer = SIPInputSerializer(data=request.data)
        if serializer.is_valid():
            investment_amount = serializer.validated_data['investment_amount']
            investment_period = serializer.validated_data['investment_period']
            annual_return_rate = serializer.validated_data['annual_return_rate']
            stepup_percentage = serializer.validated_data.get('stepup_percentage', 0.0)

            monthly_rate_of_return = annual_return_rate / 100 / 12
            months = investment_period * 12
            future_value = 0

            for i in range(1, months + 1):
                future_value += investment_amount * ((1 + monthly_rate_of_return) ** (months - i + 1))
                if i % 12 == 0:  # Apply step-up annually
                    investment_amount *= (1 + stepup_percentage / 100)

            future_value = round(future_value, 2)
            return Response({"future_value": future_value}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)