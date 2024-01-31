from django.db import models

# Create your models here.
class Movie(models.Model):
	name=models.CharField(max_length=250)
	desc=models.TextField()
	image=models.ImageField()
	movie_type=models.CharField(max_length=250)
	release_date=models.DateField()
	movie_lang=models.CharField(max_length=250)
	class Meta:
		verbose_name = "Movie"
		verbose_name_plural = "Movies"
	def __str__(self):
		return self.name
    