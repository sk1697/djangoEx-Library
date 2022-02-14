import datetime
# Create your models here.
from datetime import datetime
from common.models import CustomUser
from django.db import models
from django.utils import timezone


class Book(models.Model):
    book_name = models.CharField(null = True,max_length=100)
    book_author = models.CharField(null = True,max_length=100)
    book_kind = models.CharField(null = True,max_length=100)
    is_borrowed = models.BooleanField(default=False)
    borrowerid = models.ForeignKey(CustomUser,null = True, on_delete=models.CASCADE)
    borrower = models.CharField(null = True,max_length=100)
    borrow_date = models.DateTimeField(null = True)
    return_date = models.DateTimeField(null = True)
    #include_time = models.DateTimeField(null = True)
    def __str__(self):
        return self.book_name

    @property
    def include_time(self):
        time = datetime.now(tz=timezone.utc) - self.borrow_date

        return '+' + str(time.days + 1)+' 일'

    class Meta:
        db_table = 'Book'


