from django.urls import path
from .views import BookListView, BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('create/', BookCreateView.as_view(), name='book-create')
]
