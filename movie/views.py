from django.shortcuts import render
from .models import Movie
# Create your views here.
def movie_list(request):
	movies=Movie.objects.all()
	return render(request,'movie.html',{'movies':movies})