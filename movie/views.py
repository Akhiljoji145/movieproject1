from django.shortcuts import render
from .models import Movie
# Create your views here.
def movie_list(request):
	movies=Movie.objects.all()
	return render(request,'movie.html',{'movies':movies})

def about(request,movie_id):
	movies=Movie.objects.get(id=movie_id)
	return render(request,'moviedetail.html',{'movies':movies})