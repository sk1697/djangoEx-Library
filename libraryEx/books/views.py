from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from books.models import Book

# Create your views here.
def regBooks(request):
    return render(request, 'books/registerBook.html')

def regConBooks(request):
    name = request.POST['name']
    author = request.POST['author']

    qs = Book(book_name=name, book_author=author)
    qs.save()

    return HttpResponseRedirect(reverse('books:bookAll'))

def readBooksAll(request):
    qs = Book.objects.all()
    context = {'book_list': qs}
    return render(request,'books/readBooks.html',context)

def detBooks(request, name):
    qs = Book.objects.get(book_name= name)
    context = { 'book_info' : qs}
    return render(request,'books/detailBooks.html',context)

def modBooks(request, name):
    qs = Book.objects.get(book_name= name)
    context = { 'book_info' : qs}
    return render(request,'books/modifyBooks.html',context)

def modConBooks(request):
    name = request.POST['name']
    author = request.POST['author']

    s_qs = Book.objects.get(book_name=name)
    s_qs.book_name = name
    s_qs.book_author = author
    s_qs.save()

    return HttpResponseRedirect(reverse('books:bookAll'))

def delConBooks(request, name):
    qs = Book.objects.get(book_name=name)
    qs.delete()

    return HttpResponseRedirect(reverse('books:bookAll'))