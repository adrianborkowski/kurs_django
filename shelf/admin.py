from django.contrib import admin
from .models import Author, Publisher, Book, BookCategory, BookEdition, BookItem


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['last_name']


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(BookCategory)
admin.site.register(BookEdition)
admin.site.register(BookItem)
