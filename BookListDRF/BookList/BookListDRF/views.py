from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# You can now access individual books by their 'id'. 
# Suffix the URL path with an id of your choice from 
# the entries inside your model such as:

# http://127.0.0.1:8000/api/books/2