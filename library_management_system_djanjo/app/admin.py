from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book_name', 'author')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)