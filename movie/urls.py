from django.urls import path
from . import views
app_name='movie'
urlpatterns = [
    path('',views.movie_list,name='movie_list'),
    path('<int:movie_id>/',views.about,name='about'),
    path('add/',views.add_movie,name='add'),
    path('delete/<int:mov_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
]