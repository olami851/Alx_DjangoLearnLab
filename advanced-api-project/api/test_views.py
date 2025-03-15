from django.test import APITestCase
from .models import Book, Author, User
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date


class BookTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')  # Explicitly log in
        self.author = Author.objects.create(name="H.A. Adebanjo")
        self.book_data = {
            'title': 'A Comprehensive Guide To JavaScript',
            'author': 'self.author',
            'publication_year': 2022,
        }
        
        self.book = Book.objects.create(**self.book_data)
        
        def test_create_book(self):
            new_book_data = {
                'title': 'A Guide To Django',
                'author': 'F.M Adekoya',
                'publication_year': 2024,
            }
            
            response = self.client.post('/api/books/', new_book_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Book.objects.count(), 2)
            self.assertEqual(response.data['title'], new_book_data['title'])
        
        def test_list_books(self):
            """Test retrieving the list of books."""
            response = self.client.get('/api/books/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]['title'], self.book_data['title'])
            
        def test_retrieve_book(self):
            """Test retrieving a specific book by ID."""
            response = self.client.get(f'/api/books/{self.book.id}/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['title'], self.book_data['title'])
            
        def test_update_book(self):
            """Test updating an existing book via PUT."""
            updated_data = {
                'title': 'Harry Potter Updated',
                'publication_year': 1997,
                'author': self.author.id
            }
            response = self.client.put(f'/api/books/{self.book.id}/', updated_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.book.refresh_from_db()
            self.assertEqual(self.book.title, updated_data['title'])
            
        def test_delete_book(self):
            """Test deleting a book."""
            response = self.client.delete(f'/api/books/{self.book.id}/')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(Book.objects.count(), 0)
            
        # Validation Test
        def test_create_book_future_year(self):
            """Test that creating a book with a future year fails."""
            future_book_data = {
                'title': 'Future Book',
                'publication_year': date.today().year + 1,
                'author': self.author.id
            }
            response = self.client.post('/api/books/', future_book_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn('publication_year', response.data)
            
            # Filtering Tests
        def test_filter_by_publication_year(self):
            """Test filtering books by publication year."""
            response = self.client.get('/api/books/?publication_year=1997')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]['publication_year'], 1997)

        def test_filter_by_author(self):
            """Test filtering books by author ID."""
            response = self.client.get(f'/api/books/?author={self.author.id}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]['author'], self.author.id)

        # Searching Tests
        def test_search_by_title(self):
            """Test searching books by title."""
            response = self.client.get('/api/books/?search=Harry')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]['title'], 'Harry Potter')

        def test_search_by_author_name(self):
            """Test searching books by author name."""
            response = self.client.get('/api/books/?search=Rowling')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]['author'], self.author.id)

        # Ordering Tests
        def test_order_by_title(self):
            """Test ordering books by title."""
            Book.objects.create(title='Chamber of Secrets', publication_year=1998, author=self.author)
            response = self.client.get('/api/books/?ordering=title')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data[0]['title'], 'Chamber of Secrets')
            self.assertEqual(response.data[1]['title'], 'Harry Potter')

        def test_order_by_publication_year_desc(self):
            """Test ordering books by publication year descending."""
            Book.objects.create(title='Chamber of Secrets', publication_year=1998, author=self.author)
            response = self.client.get('/api/books/?ordering=-publication_year')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data[0]['publication_year'], 1998)
            self.assertEqual(response.data[1]['publication_year'], 1997)