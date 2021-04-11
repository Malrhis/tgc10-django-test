"""BookReviewProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import books.views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    # how to access functions from other files
    # books is the folder.
    # views is the .py file.
    # index is the function
    path('books/', books.views.show_book, name="show_book"),
    path('publishers/', books.views.show_publishers),
    path('authors/', books.views.show_authors),
    path('books/create', books.views.create_book),
    path('books/update/<book_id>', books.views.update_book,
         name="update_book"),
    path('authors/create', books.views.create_author),
    path('publishers/create', books.views.create_publisher),
    path('books/delete/<book_id>', books.views.delete_book,
         name="delete_book")
]
