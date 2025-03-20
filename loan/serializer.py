from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    
    model = Loan
    fields = '__all__'