from django.db import models
from categories.models import Category

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    isbn = models.CharField(max_length=13 ,unique=True, blank=False ,null=False)
    availability = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title