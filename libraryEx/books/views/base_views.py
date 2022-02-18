from books.models import Book
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
import urllib.request
import json

def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    book_list = Book.objects.all().order_by('-id')
    if kw:
        book_list = book_list.filter(
            Q(book_name__icontains=kw) |  # 책제목검색
            Q(book_author__icontains=kw) |  # 저자검색
            Q(book_kind__icontains=kw) |  # 책 분야검색
            Q(borrower__icontains=kw)
        ) #.distinct()

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

    # 네이버  API로 책커버 불러오기
    client_id = "7KL1lBn0_Bjs1bVyJxwL"
    client_secret = "KuQJ7WYhtZ"
    encText = urllib.parse.quote(name)
    option = "&display=1"
    url = "https://openapi.naver.com/v1/search/book?query=" + encText + option  # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request1 = urllib.request.Request(url)
    request1.add_header("X-Naver-Client-Id", client_id)
    request1.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request1)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        results = json.loads(response_body.decode('utf-8'))
        items = results.get('items')
        print(items)
        print(type(items))
        for item in items:
            imglink = item['image']
            print(imglink)
            print(type(imglink))
    else:
        print("Error Code:" + rescode)



    context = { 'book_info' : qs,
                 'imglink' : imglink
                }

    return render(request,'books/detailBooks.html',context)