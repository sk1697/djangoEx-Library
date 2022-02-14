import datetime

from books.models import Book
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


@login_required(login_url='common:login')
def bookborrow(request, bookname):

    # 도서대여 생성"
    qs = Book.objects.get(book_name = bookname)
    qs.is_borrowed = True

    CustomUser = get_user_model()
    qs.borrowerid = CustomUser.objects.get(id=request.user.pk)
    qs.borrower =CustomUser.objects.get(id=request.user.pk).korname
    qs.borrow_date = timezone.now()
    qs.return_date = qs.borrow_date + datetime.timedelta(days=14)


    print(qs)
    print(qs.id)
    print(qs.book_kind)
    print(qs.is_borrowed)
    print(qs.borrowerid)
    print(qs.borrower)
    print(qs.borrow_date)
    print(qs.return_date)
    qs.save()

    return HttpResponseRedirect(reverse('books:bookAll'))

@login_required(login_url='common:login')
def bookreturn(request, bookname):

    # 도서대여 생성"
    qs = Book.objects.get(book_name = bookname)
    qs.is_borrowed = False
    qs.borrower = None
    qs.borrow_date = None
    print(qs)
    print(qs.id)
    print(qs.is_borrowed)
    print(qs.borrower)
    print(qs.borrow_date)
    qs.save()

    return HttpResponseRedirect(reverse('books:bookAll'))