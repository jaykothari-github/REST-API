from django.http import JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def movie_list(request):

    data = list(Movie.objects.values())
    return JsonResponse({'data':data})