from django.urls import path
from .views import base_views, books_views

app_name = 'books'
urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<str:name>/det/', base_views.detBooks, name='bookDet'),


    # books_views.py
    path('reg/', books_views.regBooks, name='reg'),
    path('regCon/', books_views.regConBooks, name='regCon'),
    path('all/', books_views.readBooksAll, name='bookAll'),
    path('<str:name>/mod/', books_views.modBooks, name='bookMod'),
    path('modCon/', books_views.modConBooks, name='modCon'),
    path('<str:name>/del/', books_views.delConBooks, name='bookDel'),

]