from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Entity, Genre, Selection, Collection, Lecture
from .serializers import CourseSerializer, GenreSerializer, SelectionSerializer, CollectionSerializer, LectureSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from django.db.models import Q
from users.models import Profile
from users.serializers import UserSerializer


class AllCourse(APIView):

    def get(self, request, format=None):
        courses = Entity.objects.all()[0:4]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class AllRecomendedCourse(APIView):

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


class CourseDetail(APIView):

    def get_object(self, genre_slug, course_slug):
        try:
            return Entity.objects.filter(genre__slug=genre_slug).get(slug=course_slug)
        except Entity.DoesNotExist:
            raise Http404

    def get(self, request, genre_slug, course_slug, format=None):
        course = self.get_object(genre_slug, course_slug)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class GenreDetail(APIView):

    def get_object(self, genre_slug):
        try:
            return Genre.objects.get(slug=genre_slug)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, genre_slug, format=None):
        genre = self.get_object(genre_slug)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)


@api_view(['GET'])
def getUserSelection(request, user_id):
    selections = Selection.objects.filter(Q(user=user_id))
    courses = []
    for e in selections:
        course = Entity.objects.get(Q(id=e.course.id))
        courses.append(course)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCourseLessons(request, course_id):
    lectures = Lecture.objects.filter(Q(course=course_id))
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUserCollection(request, user_id):
    collections = Collection.objects.filter(Q(user=user_id))
    courses = []
    for c in collections:
        course = Entity.objects.get(Q(id=c.course.id))
        courses.append(course)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOwnerCourse(request, user_id):
    courses = Entity.objects.filter(Q(owner=user_id))
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


class CourseDetail(APIView):

    def get_object(self, genre_slug, course_slug):
        try:
            return Entity.objects.filter(genre__slug=genre_slug).get(slug=course_slug)
        except Entity.DoesNotExist:
            raise Http404

    def get(self, request, genre_slug, course_slug, format=None):
        course = self.get_object(genre_slug, course_slug)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class SelectionUser(APIView):

    def get(self, request, course_slug, format=None):
        selection = Selection.objects.filter(Q(course=course_slug))
        students = []
        for s in selection:
            student = Profile.objects.get(Q(id=s.user.id))
            students.append(student)
        serializer = UserSerializer(students, many=True)
        return Response(serializer.data)
