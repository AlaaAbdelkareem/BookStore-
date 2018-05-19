from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect
from store.SignUpFrom import SignUpForm 
# import models
from django.contrib.auth.models import User
from store.models import *
from store.forms import *

# import functions
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    if request.user.is_authenticated:
        MostReadBooks = Book.objects.raw('select store_book_read.book_id,store_book.id,store_book.title, count(store_book_read.book_id) as books  from store_book_read, store_book where store_book.id = store_book_read.book_id group by book_id order by books desc limit 8')
        topRatedBooks = Book.objects.raw('select store_rate.book_id,store_book.id, title, avg(rate) as rate from store_rate, store_book where store_rate.book_id = store_book.id group by book_id order by rate desc limit 8')
        topFollowedAuthors = Author.objects.raw('select store_author_follow.author_id,store_author.id, count(store_author_follow.author_id) as followers from store_author_follow, store_author where store_author.id = store_author_follow.author_id group by author_id order by followers desc limit 8')

        userBooks = Book.objects.filter(read=request.user)
        userWishs = Book.objects.filter(wish=request.user)
        userCategories = Category.objects.filter(like=request.user) 

        categories = Category.objects.all()

        return render(request, 'home.html', { 'MostReadBooks' : MostReadBooks , 'topRatedBooks': topRatedBooks, 'topFollowedAuthors' : topFollowedAuthors, 'categories': categories,'userBooks':userBooks,'userWishs':userWishs,'userCategories':userCategories})
    else:
        return redirect('login')
        

def getCategoryBooks(request, cat_id):
    if request.user.is_authenticated:
        category = get_object_or_404(Category, id=cat_id)

        show_follow = False

        try:
            category.like.get(id=request.user.id).id
        except Exception as e:
            show_follow = True

        if request.method == 'GET':
            books = Book.objects.filter(cat_books=cat_id)
            return render(request, 'category.html', {'category': category, 'show_follow': show_follow, 'books': books})
        else:
            if show_follow:
                category.like.add(request.user)
            else:
                category.like.remove(request.user)

        category.save()
        return HttpResponseRedirect('/category/' + str(cat_id))
    else:
        return redirect('login')


def allBooks(request):
    if request.user.is_authenticated:
        books = Book.objects.all()
        return render(request, 'books.html', {'books': books})
    else:
        return redirect('login')



def getBook(request, book_id):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, id=book_id)
        if request.method == 'GET':
            show_read = False
            show_wish = False

            try:
                book.read.get(id=request.user.id).id
            except Exception as e:
                show_read = True

            try:
                book.wish.get(id=request.user.id).id
            except Exception as e:
                show_wish = True

            try:
                rate=Rate.objects.get(book_id=book_id,user_id = request.user.id)
                rate_value = rate.rate
            except Exception as e:
                rate_value = 0

            return render(request, 'book.html', {'book': book, 'show_read': show_read, 'show_wish': show_wish, 'rate_value':rate_value})
        else:
            # book_id
            # request.user.book_id
            if request.POST.get('request') == 'WISH':
                book.wish.add(request.user)
                book.read.remove(request.user)
            elif request.POST.get('request') == 'RATE':
                rate_value = request.POST.get('rate')
                try:
                    rate=Rate.objects.get(book_id=book_id,user_id = request.user.id)
                    rate.rate=rate_value
                    rate.save()
                except Exception as e:
                    Rate.objects.create(rate=rate_value,book_id=book_id, user_id = request.user.id)
                return redirect('/book/'+str(book_id))
            else:
                book.read.add(request.user)
                book.wish.remove(request.user)
        book.save()
        return HttpResponseRedirect('/book/' + str(book_id))
    else:
        return redirect('login')



def author(request, author_id):
    if request.user.is_authenticated:
        author = get_object_or_404(Author, id=author_id)

        show_follow = False

        try:
            author.follow.get(id=request.user.id).id
        except Exception as e:
            show_follow = True

        if request.method == 'GET':
            books = Book.objects.filter(author_id = author.id)
            return render(request, 'author.html', {'author': author, 'show_follow': show_follow, 'books': books})
        else:
            if show_follow:
                author.follow.add(request.user)
            else:
                author.follow.remove(request.user)

        author.save()
        return HttpResponseRedirect('/author/' + str(author_id))
    else:
        return redirect('login')

# def rate(request,book_id,rate_value):

def search(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(title__icontains=request.GET.get('q'))
        return render(request, 'books.html', {'books': books})
    else:
        return redirect('login')

def edit(request):
    if request.method == 'POST':
        form = Edit(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'home.html')

    else:
        form = Edit(instance=request.user)
        context = {'form': form,
                   }
        return render(request, 'edit.html', context)


def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('updateUserPassword')
        else:
            return redirect('updateUserPassword')

    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form,
                   }
        return render(request, 'changePassword.html', context)




