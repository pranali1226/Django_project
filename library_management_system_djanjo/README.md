# Library Management System

This project is a Django-based library management system that provides a CRUD (Create, Read, Update, Delete) application for managing books in a library. 

## Features

- User authentication to manage book entries.
- Ability to add, edit, view, and delete books.
- Admin interface for managing books.

## Project Structure

```
library_management_system
├── app
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── app
│   │       ├── book_form.html
│   │       ├── book_list.html
│   │       ├── book_detail.html
│   │       └── book_confirm_delete.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── __init__.py
├── library_management_system
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd library_management_system
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install django
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser to access the admin interface:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the admin interface at `http://127.0.0.1:8000/admin/` to manage books.
- Use the app's views to create, read, update, and delete book entries.

## Testing

Run the tests using:
```
python manage.py test app
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.