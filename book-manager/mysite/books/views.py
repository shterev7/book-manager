from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, ReviewsForm
from .models import Book, Author


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')
    else:
        books = Book.objects.all()
        context = {'results': books, 'authors': Author.objects.all()}
        return render(request, 'books/index.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'books/login.html', context)


def login_user(request):
    error_message = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.filter(user=request.user)
                return render(request, 'personal/home.html', {'books': books})
            else:
                error_message = 'Your account has been disabled'
        else:
            error_message = 'Invalid login'
    return render(request, 'books/login.html', {'error_message': error_message})


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.filter(user=request.user)
                return render(request, 'books/index.html', {'books': books})
    context = {
        "form": form,
    }
    return render(request, 'books/register.html', context)


def create_book(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')
    else:

        print(request.POST)
        book = Book(title=request.POST.get('title'))
        book.author = Author.objects.get(id=request.POST.get('author'))

        book.author.save()
        book.save()

        return redirect('/books')


def create_author(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')
    else:

        print(request.POST)
        author = Author(first_name=request.POST.get('first_name'),
                        last_name=request.POST.get('last_name'))
        author.save()

        return redirect('/authors_index')


def edit_book(request, id):
    book = Book.objects.get(id=id)
    context = dict(book=book)
    return render(request, 'books/edit.html', context)


def edit_author(request, id):
    author = Author.objects.get(id=id)
    context = dict(author=author)
    return render(request, 'books/edit_authors.html', context)


def update_book(request, id):
    book = Book.objects.get(id=id)
    book.title = request.POST.get('title')
    book.author.first_name = request.POST.get('first_name')
    book.author.last_name = request.POST.get('last_name')
    book.save()
    return redirect('/books')


def update_author(request, id):
    author = Author.objects.get(id=id)
    author.first_name = request.POST.get('first_name')
    author.last_name = request.POST.get('last_name')
    author.save()
    return redirect('/authors_index')


def destroy_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books')


def destroy_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('/authors_index')


def search(request):
    q = request.GET.get("q")

    results = Book.objects.filter(Q(title__icontains=q) | Q(author__first_name__icontains=q) |
                                  Q(author__last_name__icontains=q))

    context = dict(results=results, authors=Author.objects.all(), q=q)
    return render(request, "books/index.html", context)


def authors_index(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')
    else:
        authors = Author.objects.all()
        context = {'authors': authors}
        return render(request, 'books/authors_index.html', context)


def add_review_to_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('/books/book_detail/' + str(book.id))
    else:
        form = ReviewsForm()
    return render(request, 'books/add_review_to_book.html', {'form': form})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})
