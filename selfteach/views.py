from django.shortcuts import render
from selfteachweb import settings
from .models import Book

def home(request):
    context = {
    }
    return render(request, 'selfteach/home.html', context)

def readme(request):
    context = {
    }
    return render(request, 'selfteach/readme.html', context)

def booksummary_view(request):
    ladr = Book.objects.get(author="Axler")
    context = {
        "obj":ladr,
        "basedir":settings.BASE_DIR
    }
    return render(request, 'selfteach/books.html', context)