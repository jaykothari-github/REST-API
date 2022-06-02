from django.urls import path
from . import views

urlpatterns = [
    # path('list/',views.movie_list,name='list'),
    # path('<int:pk>',views.detail,name='detail'),
    # path('list/',views.MovieListAV.as_view(),name='list'),
    # path('<int:pk>',views.MovieDetailAV.as_view(),name='detail'),
    path('list/',views.WatchListAV.as_view(),name='list'),

]
