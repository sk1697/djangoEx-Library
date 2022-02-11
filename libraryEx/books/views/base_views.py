from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from books.models import Book


def index(request):
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

def detBooks(request, name):
    qs = Book.objects.get(book_name= name)
    print(qs)
    print(qs.book_kind)
    print(qs.id)
    context = { 'book_info' : qs}
    return render(request,'books/detailBooks.html',context)