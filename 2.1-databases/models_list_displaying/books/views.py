from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

def books_view(request):
    context = {}
    template = 'books/books_list.html'
    
    return render(request, template, context)
