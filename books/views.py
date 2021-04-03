from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Publisher, Author
from .forms import BookForm, AuthorForm

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
        create_book_form = BookForm(request.POST)

        # check if the form has valid values
        if create_book_form.is_valid():
            create_book_form.save()
            return redirect(reverse(index))
        else:
            # if does not have valid values, re-render the form
            return render(request, 'books/create_book.template.html', {
                'form': create_book_form
            })
    else:
        create_book_form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': create_book_form
        })


def create_author(request):
    create_author_form = AuthorForm()

    if request.method == 'POST':
        create_author_form = AuthorForm(request.POST)

        # check if the form has valid values
        if create_author_form.is_valid():
            create_author_form.save()
            return redirect(reverse(index))
        else:
            # if does not have valid values, re-render the form
            return render(request, 'books/create_author.template.html', {
                'form': create_author_form
            })
    else:
        create_author_form = AuthorForm()
        return render(request, 'books/create_author.template.html', {
            'form': create_author_form
        })

    return render(request, 'books/create_author.template.html', {
        'form': create_author_form
    })
