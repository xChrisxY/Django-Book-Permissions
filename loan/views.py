from .models import Loan
from .serializer import LoanSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class LoanViewSet(viewsets.ModelViewSet):
    
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]