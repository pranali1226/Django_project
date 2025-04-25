# filepath: C:\ENV_TY_IT\library_management_system\app\forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'published_date', 'isbn']
        