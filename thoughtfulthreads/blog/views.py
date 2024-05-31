from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Post, Category
from .models import Post, Rating
from .forms import RatingForm


# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    ratings = Rating.objects.filter(post=post)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.post = post
            rating.save()
            return redirect('post', url=post.url)  # Redirect to the same post page
    else:
        form = RatingForm()

    return render(request, 'posts.html', {'post': post, 'cats': cats, 'ratings': ratings, 'form': form})

def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})


def add_rating(request, url):
    post = Post.objects.get(url=url)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.post = post
            rating.save()
            return redirect('post', url=url)
    else:
        form = RatingForm()

    return render(request, 'rating.html', {'form': form})