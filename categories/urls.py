from django.urls import path
from .views import CategoryListView, CategoryCreateView

urlpatterns = [
    path('', CategoryListView.as_view(), name='list-categories'),
    path('create/', CategoryCreateView.as_view(), name='category-create')
]
