import datetime

from books.models import Book
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail

@login_required(login_url='common:login')
def bookborrow(request, bookname):

    # 도서대여 생성"
    qs = Book.objects.get(book_name = bookname)
    qs.is_borrowed = True

    CustomUser = get_user_model()
    qs.borrowerid = CustomUser.objects.get(id=request.user.pk)
    qs.borrower =CustomUser.objects.get(id=request.user.pk).korname
    print(CustomUser.objects.get(id=request.user.pk).email)
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

    # 대여정보 메일 발송
    # email_subject = str(qs.borrower) + '님  "' + str(qs) + '"  도서대여 정보입니다.'
    # email_content = '안녕하세요. flagship4G 도서관리자입니다. \n\n"'+ str(qs) + '" 도서를 대여하셨습니다. \n대출기간은 14일이니 참고 부탁드립니다. \n'
    # email_sender = 'sk1697@naver.com'
    # email_reciever = str(CustomUser.objects.get(id=request.user.pk).email)
    # send_mail(email_subject,
    #           email_content,
    #           email_sender,
    #           [email_reciever],
    #           fail_silently=False
    #           )


    return HttpResponseRedirect(reverse('books:bookAll'))

@login_required(login_url='common:login')
def bookreturn(request, bookname):

    # 도서반납 처리
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

    # 도서반납확인 메일 발송
    # CustomUser = get_user_model()
    # email_subject = str(CustomUser.objects.get(id=request.user.pk).korname) + '님  "' + str(qs) + '"  도서반납 확인 메일입니다.'
    # email_content = '안녕하세요. flagship4G 도서관리자입니다. \n\n"'+ str(qs) + '" 도서를 반납하셨습니다. \n 그룹서가를 이용해주셔서 감사합니다 ^ㅡ^ \n'
    # email_sender = 'sk1697@naver.com'
    # email_reciever = str(CustomUser.objects.get(id=request.user.pk).email)
    # send_mail(email_subject,
    #           email_content,
    #           email_sender,
    #           [email_reciever],
    #           fail_silently=False
    #           )

    return HttpResponseRedirect(reverse('books:bookAll'))
