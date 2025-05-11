from django.contrib import admin
from .models import Book, Category, Review, BorrowedBook

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'borrowing_price')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('review_text', 'book__title', 'user__username')

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrow_date', 'returned_date')
    list_filter = ('borrow_date', 'returned_date')
    search_fields = ('book__title', 'user__username')
