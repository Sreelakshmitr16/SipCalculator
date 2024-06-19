from rest_framework import serializers

class SIPInputSerializer(serializers.Serializer):
    investment_amount = serializers.FloatField()
    investment_period = serializers.IntegerField()
    annual_return_rate = serializers.FloatField()
    stepup_percentage = serializers.FloatField(required=False, default=0.0)