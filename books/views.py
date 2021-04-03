from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Publisher, Author
from .forms import BookForm

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


def show_authors(request):
    all_authors = Author.objects.all()
    return render(request, 'books/show_authors.template.html', {
        'all_authors': all_authors
    })


def create_book(request):
    if request.method == 'POST':
        create_form = BookForm(request.POST)

        # check if the form has valid values
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            # if does not have valid values, re-render the form
            return render(request, 'books/create.template.html', {
                'form': create_form
            })
    else:
        create_form = BookForm()
        return render(request, 'books/create.template.html', {
            'form': create_form
        })
