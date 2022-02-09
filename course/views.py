from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Entity, Genre, Selection, Wishlist, Lecture
from .serializers import CourseSerializer, GenreSerializer, SelectionSerializer, WishlistSerializer, LectureSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from django.db.models import Q
from users.models import Profile
from users.serializers import UserSerializer
import datetime
from rest_framework import status


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
        collections = Wishlist.objects.all()[0:4]
        serializer = WishlistSerializer(collections, many=True)
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
def getUserWishlist(request, user_id):
    collections = Wishlist.objects.filter(Q(user=user_id))
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


@api_view(['POST'])
def createCourse(request):
    future_course = Entity()
    owner = Profile.objects.get(Q(id=request.data['ownerId']))
    genre = Genre.objects.get(Q(id="869d268e-09f6-4177-96b4-585707e85545"))
    future_course.owner = owner
    future_course.title = request.data['title']
    future_course.description = request.data['description']
    future_course.slug = 3
    future_course.cover_img = "profiles/project-1.jpg"
    future_course.created_time = datetime.timedelta(days=30)
    future_course.genre = genre
    future_course.save()
    return Response('createCourse!')


@api_view(['POST'])
def updateCourse(request, pk):
    print(request.data)
    print(request.data)
    print(request.data)
    print(request.data)
    return None


@api_view(['POST'])
def deleteCourse(request):
    course = Entity.objects.get(Q(id=request.data['courseId']))
    course.delete()
    return Response('Tag was deleted!')


@api_view(['GET'])
def getSerialNumber(request):
    courses = Entity.objects.filter(Q(owner=user_id))
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def registerCourse(request):
    try:
        user = Profile.objects.get(Q(id=request.data['userId']))
        course = Entity.objects.get(Q(serial_number=request.data['serialNumber']))
    except Exception:
        return Response('Not Existed', status=status.HTTP_201_CREATED)
    try:
        existed_selection = Selection.objects.get(Q(user=user.id) & Q(course=course.id))
        if existed_selection:
            return Response('Register Before', status=status.HTTP_201_CREATED)
    except Exception:
        try:
            wishlist = Wishlist.objects.get(Q(user=user.id) & Q(course=course.id))
            wishlist.delete()
        except Exception:
            print('wishlist was deleted!')
        new_selection = Selection()
        new_selection.user = user
        new_selection.course = course
        new_selection.select_time = datetime.timedelta(days=30)
        new_selection.save()
    return Response('Register Success.')


@api_view(['POST'])
def getCourseStatus(request):
    try:
        selection = Selection.objects.get(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
        return Response(1)
    except Exception:
        return Response(0)


@api_view(['POST'])
def getWishlistStatus(request):
    try:
        wishlist = Wishlist.objects.get(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
        return Response(1)
    except Exception:
        return Response(0)


@api_view(['POST'])
def addWishlist(request):
    try:
        wishlist = Wishlist.objects.get(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
        return Response(0)
    except Exception:
        new_wishlist = Wishlist()
        user = Profile.objects.get(Q(id=request.data['userId']))
        course = Entity.objects.get(Q(id=request.data['courseId']))
        new_wishlist.user = user
        new_wishlist.course = course
        new_wishlist.collect_time = datetime.timedelta(days=30)
        new_wishlist.save()
        return Response(1)


@api_view(['POST'])
def removeWishlist(request):
    try:
        wishlist = Wishlist.objects.get(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
        wishlist.delete()
        return Response(1)
    except Exception:
        return Response(0)
