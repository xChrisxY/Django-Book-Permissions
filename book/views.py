from .models import Book
from .serializer import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'category', 'availability']