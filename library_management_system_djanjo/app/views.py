from django.shortcuts import render, get_object_or_404, redirect
from .models import Book  # Corrected from 'books' to 'Book'
from .forms import BookForm # Assuming you have a form for the Book model

# Example view for listing books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'app/book_list.html', {'books': books})

# Example view for book details
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'app/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)  # Don't save to the database yet
            book.user = request.user       # Set the logged-in user as the book's user
            book.save()                    # Save the book to the database
            return redirect('book_list')   # Redirect to the book list view
    else:
        form = BookForm()
    return render(request, 'app/book_create.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list view
    else:
        form = BookForm(instance=book)
    return render(request, 'app/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list view
    return render(request, 'app/book_confirm_delete.html', {'book': book})
# Compare this snippet from library_management_system/app/views.py:
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import books
# from .forms import BookForm
#
# # Example view for listing books
# def book_list(request):
#     books = books.objects.all()
#     return render(request, 'app/book_list.html', {'books': books})
#
# # Example view for book details
# def book_detail(request, pk): # Assuming pk is the primary key for books
#     book = get_object_or_404(books, pk=pk)
#     return render(request, 'app/book_detail.html', {'book': book})
#
# def book_create(request):
#     if request.method == 'POST':