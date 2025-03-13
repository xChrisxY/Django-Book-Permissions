from django.db import models
from book.models import Book
from users.models import UserModel

# Create your models here.
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="loans")
    borrored_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    return_date = models.DateTimeField(blank=False, null=False)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Loan of {self.book.title} by {self.user.username}"

    

    
