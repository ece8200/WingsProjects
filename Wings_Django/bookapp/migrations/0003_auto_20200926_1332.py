# Generated by Django 3.1.1 on 2020-09-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='book',
        ),
        migrations.AddField(
            model_name='category',
            name='book',
            field=models.ManyToManyField(to='bookapp.Book'),
        ),
    ]
