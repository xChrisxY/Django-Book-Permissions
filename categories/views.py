from rest_framework import generics
from .models import Category
from .serializer import CategorySerializer

# Create your views here.
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
