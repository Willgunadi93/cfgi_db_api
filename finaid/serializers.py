from rest_framework.serializers import ModelSerializer
from .models import Finaid

class FinaidSerializer(ModelSerializer):
    class Meta:
        model = Finaid
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'int_identity', 'college', 'degree' , 'other' , 'fieldof_study', 'graduation_year', 'marital', 'children', 'immigrant_status', 'amount' , 'reason']