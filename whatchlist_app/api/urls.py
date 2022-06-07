from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # path('list/',views.movie_list,name='list'),
    # path('<int:pk>',views.detail,name='detail'),
    # path('list/',views.MovieListAV.as_view(),name='list'),
    # path('<int:pk>',views.MovieDetailAV.as_view(),name='detail'),
    path('list/',views.WatchListAV.as_view(),name='list'),
    path('<int:pk>',views.WatchDetailAV.as_view(),name='detail'),
    path('srmpl-list/',views.StreamPlListAV.as_view(),name='srmpl-list'),
    path('srmpl/<int:pk>',views.StreamPlDetailAV.as_view(),name='streamplatform-detail'),
    path('review/',views.ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>',views.ReviewDetail.as_view(),name='review-detail'),

]
