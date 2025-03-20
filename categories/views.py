from .models import Category
from .serializer import CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

