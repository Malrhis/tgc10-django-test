from django.contrib import admin
from .models import Book
from .models import Publisher
from .models import Author
from .models import Genre
from .models import Tag

# Register your models here.
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Tag)
