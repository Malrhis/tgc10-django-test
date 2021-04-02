from django.db import models

# Create your models here.
# Model represent one entity in ER diagram
# Which in turn has one table in mysql

# class is a generic entity.


class Book(models.Model):
    # Create "columns" in class in models.py
    # definte a VARCHAR using Django
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)

    # TextField is the TEXT in MySQL
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    # what are the columns for Publisher table?
    name = models.CharField(blank=False, max_length=255)
    email = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
