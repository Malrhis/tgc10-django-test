# Generated by Django 3.1.7 on 2021-04-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.Tag'),
        ),
    ]
