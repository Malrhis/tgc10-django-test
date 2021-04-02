from django.shortcuts import render
from .models import Book, Publisher

# Create your views here.

# define a view function


def index(request):
    # create a query set that has all the books
    # a query set is like a cursor
    books = Book.objects.all()
    return render(request, 'books/index-template.html', {
        'books': books
    })


def show_publishers(request):
    all_publishers = Publisher.objects.all()
    return render(request, 'books/show_publishers.template.html', {
        'all_publishers': all_publishers
    })
