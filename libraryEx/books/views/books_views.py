from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from books.models import Book
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url='common:login')
def regBooks(request):
    return render(request, 'books/registerBook.html')

@login_required(login_url='common:login')
def regConBooks(request):
    name = request.POST['name']
    author = request.POST['author']

    qs = Book(book_name=name, book_author=author)
    qs.save()

    return HttpResponseRedirect(reverse('books:bookAll'))

def readBooksAll(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    book_list = Book.objects.all().order_by('-id')
    if kw:
        book_list = book_list.filter(
            Q(book_name__icontains=kw) |  # 책제목검색
            Q(book_author__icontains=kw)  # 저자검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(book_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # qs = Book.objects.all()
    context = {'book_list': page_obj, 'page': page, 'kw': kw}
    return render(request,'books/readBooks.html',context)


@login_required(login_url='common:login')
def modBooks(request, name):
    qs = Book.objects.get(book_name= name)
    context = { 'book_info' : qs}
    return render(request,'books/modifyBooks.html',context)

@login_required(login_url='common:login')
def modConBooks(request):
    name = request.POST['name']
    author = request.POST['author']

    s_qs = Book.objects.get(book_name=name)
    s_qs.book_name = name
    s_qs.book_author = author
    s_qs.save()

    return HttpResponseRedirect(reverse('books:bookAll'))

@login_required(login_url='common:login')
def delConBooks(request, name):
    qs = Book.objects.get(book_name=name)
    qs.delete()

    return HttpResponseRedirect(reverse('books:bookAll'))