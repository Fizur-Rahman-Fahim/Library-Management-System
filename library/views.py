from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from .models import Book, Category, BorrowedBook
from user.models import UserProfile

def home(request):
    books = Book.objects.all()[:6]  # Get latest 6 books
    categories = Category.objects.all()
    return render(request, 'library/home.html', {
        'books': books,
        'categories': categories
    })

def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search')
    category_query = request.GET.get('category')
    
    if search_query:
        books = books.filter(title__icontains=search_query)
    
    if category_query:
        books = books.filter(category_id=category_query)
    
    return render(request, 'library/book_list.html', {
        'books': books,
        'categories': categories
    })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def category_books(request, pk):
    category = get_object_or_404(Category, pk=pk)
    books = Book.objects.filter(category=category)
    return render(request, 'library/category_books.html', {
        'category': category,
        'books': books
    })

@login_required
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    
    # Check if book is already borrowed
    if BorrowedBook.objects.filter(book=book, returned_date=None).exists():
        messages.error(request, 'This book is currently not available.')
        return redirect('library:book_detail', pk=pk)
    
    # Check if user has enough balance
    if user.balance < book.borrowing_price:
        messages.error(request, f'Insufficient balance. You need ${book.borrowing_price} to borrow this book.')
        return redirect('user:deposit_money')
    
    # Process the transaction
    user.balance -= book.borrowing_price
    user.save()
    
    BorrowedBook.objects.create(book=book, user=user)
    messages.success(request, f'Successfully borrowed "{book.title}". ${book.borrowing_price} has been deducted from your balance.')
    return redirect('library:book_detail', pk=pk)

@login_required
def return_book(request, pk):
    borrowed_book = get_object_or_404(BorrowedBook, pk=pk, user=request.user, returned_date=None)
    borrowed_book.return_book()  # This method will be added to the BorrowedBook model
    messages.success(request, f'Successfully returned "{borrowed_book.book.title}".')
    return redirect('library:borrowed_books')

@login_required
def user_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return render(request, 'library/profile.html', {
        'profile': profile,
        'borrowed_books': borrowed_books
    })

@login_required
def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user).order_by('-borrow_date')
    return render(request, 'library/borrowed_books.html', {
        'borrowed_books': borrowed_books
    })