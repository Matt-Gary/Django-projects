# Bookstore REST API in Django
## Introduction
This project aims to create a simple yet powerful REST API application for a bookstore using Django. The application allows users to list and create books, as well as view, update, and delete individual books using unique identifiers.
## Technologies Used
* Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
* Django Rest Framework (DRF): A powerful and flexible toolkit for building Web APIs in Django.
* Python 3: The programming language used for developing the application.
## What I Learned
* Leveraging Django and Django Rest Framework for building robust and scalable RESTful APIs.
* Implementing generic views in DRF to simplify common CRUD operations.
* Creating serializers to handle data conversion between complex types and Python datatypes.
* Utilizing Django models for database interactions and schema definition.
## Usage
To access the API, run the Django development server and navigate to the specified URL:

* List and create books: http://127.0.0.1:8000/api/books/
* Retrieve, update, and delete a specific book: http://127.0.0.1:8000/api/books/{book_id}/
* Replace `{book_id}` with the desired book's ID.

![image](https://github.com/Matt-Gary/Django-projects/assets/121462847/8af3869a-13e8-4e72-af4f-df627a92f9be)

## Conclusion
This project serves as a foundation for a bookstore API and demonstrates the power and simplicity of Django and Django Rest Framework. It provides a solid starting point for further enhancements and customization in the realm of web development.
