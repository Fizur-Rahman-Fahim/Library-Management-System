from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('category/<int:pk>/', views.category_books, name='category_books'),
    path('borrow/<int:pk>/', views.borrow_book, name='borrow_book'),
    path('profile/', views.user_profile, name='profile'),
    path('my-books/', views.borrowed_books, name='borrowed_books'),
    path('return/<int:pk>/', views.return_book, name='return_book'),
]