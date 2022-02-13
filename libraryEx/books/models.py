import datetime
from django.db import models
from django.contrib.auth.models import User
from common.models import CustomUser
from django.utils import timezone
# Create your models here.



class Book(models.Model):
    book_name = models.CharField(null = True,max_length=100)
    book_author = models.CharField(null = True,max_length=100)
    book_kind = models.CharField(null = True,max_length=100)
    is_borrowed = models.BooleanField(default=False)
    borrowerid = models.ForeignKey(CustomUser,null = True, on_delete=models.CASCADE)
    borrower = models.CharField(null = True,max_length=100)
    borrow_date = models.DateTimeField(null = True)
    return_date = models.DateTimeField(null = True)

    def __str__(self):
        return self.book_name

# class Borrow(models.Model):
#     is_borrowed = models.BooleanField(default=False)
#     borrower = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     borrow_date = models.DateTimeField()
#     borrow_book = models.ForeignKey(Book,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.borrow_book


