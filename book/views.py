from rest_framework import generics
from .models import Book
from .serializer import BookSerializer
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDestroyView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
