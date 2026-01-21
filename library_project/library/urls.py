from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/add/', views.AuthorCreateView.as_view(), name='author-add'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/add/', views.BookCreateView.as_view(), name='book-add'),
    path('borrow/', views.BorrowListView.as_view(), name='borrow-list'),
    path('borrow/add/', views.BorrowCreateView.as_view(), name='borrow-add'),
    path('export/', views.ExportExcelView.as_view(), name='export-excel'),
]