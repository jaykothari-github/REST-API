from django.http import JsonResponse
from ..models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

'''------------------------------ Function Based Views ------------------------------------'''
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all() 
#         serializer = MovieSerializer(movies,many=True)
#         # print(serializer.data)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serial = MovieSerializer(data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serial.errors)

# @api_view(['GET','PUT','DELETE'])
# def detail(request,pk):
#     try:
#         movie = Movie.objects.get(id=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serial = MovieSerializer(movie)
#         return Response(serial.data)

#     elif request.method == 'PUT':
#         serial = MovieSerializer(instance=movie,data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data)
#         else: return Response(serial.errors)

#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response('Data Deleted',status=status.HTTP_204_NO_CONTENT)

''' -------------------------------- Generic Views ---------------------------------- '''

# class MovieListAV(APIView):

#     def get(self,request):
#         movies = Movie.objects.all()
#         serial = MovieSerializer(movies,many=True)
#         return Response(serial.data)

#     def post(self,request):
#         serial = MovieSerializer(data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serial.errors)

# class MovieDetailAV(APIView):

#     def get(self,request,pk):
#         try:
#             movie = Movie.objects.get(id=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serial = MovieSerializer(movie)
#         return Response(serial.data)

#     def put(self,request,pk):
#         try:
#             movie = Movie.objects.get(id=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serial = MovieSerializer(instance=movie,data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data)
#         else: return Response(serial.errors)

#     def delete(self,request,pk):
#         try:
#             movie = Movie.objects.get(id=pk)
#             movie.delete()
#             return Response('Data Deleted',status=status.HTTP_204_NO_CONTENT)

#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)


''' ---------------------------------- New Models -------------------------------------------- '''

class WatchListAV(APIView):

    def get(self,request):
        wl = Watchlist.objects.all()
        serial = WatchListSerializer(wl,many=True)
        return Response(serial.data)

    def post(self,request):
        serial = WatchListSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors)
