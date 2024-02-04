from django.shortcuts import render,redirect
from .models import Movie
from django.urls import reverse
from .forms import MovieForm
# Create your views here.
def movie_list(request):
	movies=Movie.objects.all()
	return render(request,'movie.html',{'movies':movies})

def about(request,movie_id):
	movies=Movie.objects.get(id=movie_id)
	return render(request,'moviedetail.html',{'movies':movies})

def add_movie(request):
	if request.method=='POST':
		name=request.POST.get('name',)
		desc=request.POST.get('desc',)
		image=request.FILES.get('image')
		movie_type=request.POST.get('movie_type',)
		release_date=request.POST.get('release_date',)
		movie_lang=request.POST.get('movie_lang',)
		movie=Movie(name=name,desc=desc,image=image,movie_type=movie_type,release_date=release_date,movie_lang=movie_lang)
		movie.save()
		return redirect('/')
	return render(request,'addmovie.html')

def delete(request,mov_id):
	movie=Movie.objects.get(id=mov_id)
	movie.delete()
	return redirect('/')

def update(request,id):
	movie=Movie.objects.get(id=id)
	form=MovieForm(request.POST or None,request.FILES,instance=movie)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request,'update.html',{'movie':movie,'form':form})