from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.book_name} by {self.author}"