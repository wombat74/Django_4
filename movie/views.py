from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm

def home(request):
    searchTerm = request.GET.get('searchMovie')

    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    context = {
        'searchTerm':searchTerm,
        'movies':movies
    }

    return render(request, 'home.html', context)

def about(request):
    return HttpResponse('<h1>Welcome to the About Page!</h1>')

def signup(request):
    email = request.GET.get('email')

    context = {
        'email':email
    }
    
    return render(request, 'signup.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    reviews = Review.objects.filter(movie = movie)

    context = {
        'movie': movie,
        'reviews': reviews
    }

    return render(request, 'detail.html', context)

def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'GET':
        return render(request, 'createreview.html', {'form':ReviewForm(),
                                                     'movie':movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('detail', newReview.movie.id)
        except ValueError:
            return render(request,'createreview.html',{'form':ReviewForm(),
                                                       'error':'bad data passed in'})

def updatereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return (render, 'updatereview.html', {'review':review, 'form':form})
