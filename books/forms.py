from django import forms
from .models import Book, Author, Publisher


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'desc', 'ISBN', 'genre', 'tags')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'dob')


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = {'name', 'email'}
