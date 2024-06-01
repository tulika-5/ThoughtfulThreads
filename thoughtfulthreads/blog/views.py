from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Category
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Post, Like, ReadLater,UserProfile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "CONGRATULATIONS, You are Registered!")
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    messages.error(request, "Invalid username or password")
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/home/')

def user_profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    context = {
        'user': user,
        'user_profile': user_profile,
    }
    return render(request, 'userprofile.html', context)
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return JsonResponse({'liked': created})

@login_required
def save_for_later(request, post_id):
    post = Post.objects.get(pk=post_id)
    read_later, created = ReadLater.objects.get_or_create(user=request.user, post=post)
    if not created:
        read_later.delete()
    return JsonResponse({'saved': created})

def home(request):
    # load all the posts from db (limit to 10)
    posts = Post.objects.all()[:10]
    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})


def term_and_condition(request):
    return render(request, 'term&condition.html')


def privacy(request):
    return render(request, 'privacy.html')


def about(request):
    return render(request, 'about.html')
