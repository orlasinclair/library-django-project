from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BorrowBookForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    data = {'books': Book.objects.all()}
    return render(request, 'home.html', data)

@login_required
def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        print(book)
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            book.borrower = request.user
            book.save()
            return redirect("library-show", book_id=book_id)
    else:
        form = BorrowBookForm(initial={'borrower': request.user})
    data = {
        'book': book,
        'form': form
    }
    return render(request, 'book.html', data)

@login_required
def return_book(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    print(book)
    book.borrower=None
    book.save()
    return redirect("library-show", book_id=book_id)




def not_found_404(request, exception):
    data = {'err': exception}
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')


