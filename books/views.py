from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Publisher, Author
from .forms import BookForm, AuthorForm, PublisherForm

# Create your views here.

# define a view function


def show_book(request):
    # create a query set that has all the books
    # a query set is like a cursor
    books = Book.objects.all()
    return render(request, 'books/show-book.template.html', {
        'books': books
    })


def create_book(request):
    if request.method == 'POST':
        create_book_form = BookForm(request.POST)

        # check if the form has valid values
        if create_book_form.is_valid():
            create_book_form.save()
            return redirect(reverse(show_book))
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


def update_book(request, book_id):
    # Check if form is submitted
    if request.method == 'POST':
        book_being_updated = get_object_or_404(Book, pk=book_id)
        book_being_update_title = book_being_updated.title
        update_form = BookForm(request.POST, instance=book_being_updated)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse(show_book))
        else:
            return render(request, 'books/update-book.template.html', {
                'book_form': update_form,
                'book_title': book_being_update_title
            })
    else:
        # all i want is to display
        # 1. Retrieve publisher to update from DB
        book_to_update = get_object_or_404(Book, pk=book_id)
        # 2. create form and initialise its fields with the book data
        book_title = book_to_update.title
        book_form = BookForm(instance=book_to_update)

        # render the form
        return render(request, 'books/update-book.template.html', {
            'book_form': book_form,
            'book_title': book_title
        })


def delete_book(request, book_id):
    book_to_delete = get_object_or_404(Book, pk=book_id)

    return render(request, 'books/delete-book.template.html', {
        'book_to_delete': book_to_delete,
    })


def show_publishers(request):
    all_publishers = Publisher.objects.all()
    return render(request, 'books/show_publishers.template.html', {
        'all_publishers': all_publishers
    })


def create_publisher(request):
    if request.method == 'POST':
        create_publisher_form = PublisherForm(request.POST)
        if create_publisher_form.is_valid():
            create_publisher_form.save()
            return HttpResponse("New publisher Created")
        else:
            return HttpResponse("Form not valid")
    else:
        form = PublisherForm()
        return render(request, 'books/create_publisher.template.html', {
            'form': form
        })


def show_authors(request):
    all_authors = Author.objects.all()
    return render(request, 'books/show_authors.template.html', {
        'all_authors': all_authors
    })


def create_author(request):
    create_author_form = AuthorForm()

    if request.method == 'POST':
        create_author_form = AuthorForm(request.POST)

        # check if the form has valid values
        if create_author_form.is_valid():
            create_author_form.save()
            return redirect(reverse(show_book))
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
