from django.test import TestCase
from .models import books
from django.urls import reverse

class BookModelTest(TestCase):

    def setUp(self):
        self.book = books.objects.create(
            user='testuser',
            book_name='Test Book',
            author='Test Author'
        )

    def test_book_creation(self):
        self.assertEqual(self.book.book_name, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')

    def test_string_representation(self):
        self.assertEqual(str(self.book), 'Test Book by Test Author')


class BookViewTest(TestCase):

    def setUp(self):
        self.book = books.objects.create(
            user='testuser',
            book_name='Test Book',
            author='Test Author'
        )

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_book_create_view(self):
        response = self.client.post(reverse('book_create'), {
            'book_name': 'New Book',
            'author': 'New Author'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(books.objects.filter(book_name='New Book').exists())

    def test_book_update_view(self):
        response = self.client.post(reverse('book_update', args=[self.book.id]), {
            'book_name': 'Updated Book',
            'author': 'Updated Author'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.book.refresh_from_db()
        self.assertEqual(self.book.book_name, 'Updated Book')

    def test_book_delete_view(self):
        response = self.client.post(reverse('book_delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(books.objects.filter(id=self.book.id).exists())