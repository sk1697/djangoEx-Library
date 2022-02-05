from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index),
    path('reg/', views.regBooks, name='reg'),
    path('regCon/', views.regConBooks, name='regCon'),
    path('all/', views.readBooksAll, name='bookAll'),
    path('<str:name>/det/', views.detBooks, name='bookDet'),
    path('<str:name>/mod/', views.modBooks, name='bookMod'),
    path('modCon/', views.modConBooks, name='modCon'),
    path('<str:name>/del/', views.delConBooks, name='bookDel'),

]