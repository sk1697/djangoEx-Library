from books.models import Book
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render

@login_required(login_url='common:login')
def borrow_create(request, bookname):

    # 도서대여 생성"
    qs = Book.objects.get(book_name = bookname)
    qs.is_borrowed = True
    qs.borrower = request.user
    qs.borrow_date = timezone.now()
    print(qs)
    print(qs.id)
    print(qs.book_kind)
    print(qs.is_borrowed)
    print(qs.borrower)
    print(qs.borrow_date)
    qs.save()

    return HttpResponseRedirect(reverse('books:bookAll'))

@login_required(login_url='common:login')
def borrow_delete(request, bookname):

    # 도서대여 생성"
    qs = Book.objects.get(book_name = bookname)
    qs.is_borrowed = False

    qs.borrower = None
    qs.borrow_date = timezone.now()
    print(qs)
    print(qs.id)
    print(qs.book_kind)
    print(qs.is_borrowed)
    print(qs.borrower)
    print(qs.borrow_date)
    qs.save()

    return HttpResponseRedirect(reverse('books:bookAll'))