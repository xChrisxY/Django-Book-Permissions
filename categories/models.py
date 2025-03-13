from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.name 