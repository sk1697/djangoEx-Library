import datetime
from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)
    #book_relDate = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.book_name

