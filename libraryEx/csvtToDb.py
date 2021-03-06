import csv
import os
import django
import sys

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "libraryEx.settings")  # 1. 여기서 프로젝트명.settings입력
django.setup()

# 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과

from books.models import *  # 2. App이름.models

CSV_PATH = './booklist.csv'  # 3. csv 파일 경로

with open(CSV_PATH, newline='') as csvfile:  # 4. newline =''
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        print(row)
        qs = Book.objects.create(  # 5. class명.objects.create
            book_name=row['book_name'],
            book_author = row['book_author'],
            book_kind = row['book_kind'],
        )
        qs.save()