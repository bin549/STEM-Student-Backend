from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Entity, Genre, Selection, Collection
from .serializers import CourseSerializer, GenreSerializer, SelectionSerializer, CollectionSerializer


class AllCourse(APIView):

    def get(self, request, format=None):
        courses = Entity.objects.all()[0:4]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class AllGenre(APIView):

    def get(self, request, format=None):
        genres = Genre.objects.all()[0:4]
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class AllSelection(APIView):

    def get(self, request, format=None):
        selections = Selection.objects.all()[0:4]
        serializer = SelectionSerializer(selections, many=True)
        return Response(serializer.data)


class AllCollection(APIView):

    def get(self, request, format=None):
        collections = Collection.objects.all()[0:4]
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
