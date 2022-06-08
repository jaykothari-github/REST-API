from django.http import JsonResponse
from ..models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


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

class WatchDetailAV(APIView):

    def get(self,request,pk):
        try:
            wl = Watchlist.objects.get(id=pk)
            serial = WatchListSerializer(wl)
            return Response(serial.data)
        except:
            return Response('Invalid Data ID',status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        wl = Watchlist.objects.get(id=pk)
        serial = WatchListSerializer(instance=wl,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors)

    def delete(self,request,pk):
        try:
            wl = Watchlist.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        wl.delete()
        return Response('Data Deleted',status=status.HTTP_404_NOT_FOUND)


class StreamPlListAV(APIView):

    def get(self,request):
        wl = StreamPlatform.objects.all()
        serial = StreamPlatformSerializer(wl,many=True,context={'request':request})
        return Response(serial.data)

    def post(self,request):
        serial = StreamPlatformSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors)

class StreamPlDetailAV(APIView):

    def get(self,request,pk):
        try:
            wl = StreamPlatform.objects.get(id=pk)
            serial = StreamPlatformSerializer(wl,context={'request':request})
            return Response(serial.data)
        except:
            return Response('Invalid Data ID',status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        wl = StreamPlatform.objects.get(id=pk)
        serial = StreamPlatformSerializer(instance=wl,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors)

    def delete(self,request,pk):
        try:
            wl = StreamPlatform.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        wl.delete()
        return Response('Data Deleted',status=status.HTTP_404_NOT_FOUND)

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


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
