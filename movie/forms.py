from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','desc','image','movie_type','release_date','movie_lang']
    