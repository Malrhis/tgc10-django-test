# Generated by Django 3.1.7 on 2021-04-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='email',
            field=models.EmailField(max_length=320),
        ),
    ]
