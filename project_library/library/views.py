from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    data = {'books': Book.objects.all()}
    return render(request, 'home.html', data)

@login_required
def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    data ={ 'book': book}
    return render(request, 'book.html', data)

def not_found_404(request, exception):
    data = {'err': exception}
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')


