from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Entity, Genre, Selection, Wishlist, Lecture, Format
from .serializers import CourseSerializer, GenreSerializer, SelectionSerializer, WishlistSerializer, LectureSerializer, FormatSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from django.db.models import Q
from users.models import Profile
from users.serializers import UserSerializer
import datetime
from rest_framework import status
from homework.models import Assignment, Execution
from .utils import paginateCourses
import random


class AllCourse(APIView):

    def get(self, request, format=None):
        courses = Entity.objects.all()[0:4]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class AllVisibleCourse(APIView):

    def get(self, request, format=None):
        courses = Entity.objects.filter(Q(is_visible=True))
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


@api_view(['GET'])
def getCourseDetail(request, course_name):
    try:
        course = Entity.objects.get(title=course_name)
        serializer = CourseSerializer(course, many=False)
        return Response(serializer.data)
    except Entity.DoesNotExist:
        raise Http404



class CourseDetail(APIView):

    def get_object(self, course_id):
        try:
            return Entity.objects.get(id=course_id)
        except Entity.DoesNotExist:
            raise Http404

    def get(self, request, course_id, format=None):
        course = self.get_object(course_id)
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
def getCourseLectures(request, course_id):
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
    genre = Genre.objects.get(Q(id="169d268e-09f6-4177-96b4-585707e85545"))
    future_course.owner = owner
    future_course.title = request.data['title']
    future_course.description = request.data['description']
    future_course.cover_img = "profiles/project-9.jpg"
    future_course.created_time = datetime.timedelta(days=30)
    future_course.genre = genre
    future_course.serial_number = int(random.random()*1000000)
    future_course.is_visible = True
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
        homeworks = Assignment.objects.filter(Q(course=course.id))
        for homework in homeworks:
            execution = Execution()
            execution.homework = homework
            execution.user = user
            execution.save()
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


@api_view(['POST'])
def getCourseVisibleStatus(request):
    try:
        course = Entity.objects.get(Q(id=request.data['courseId']))
        if course.is_visible:
            return Response(1)
        return Response(0)
    except Exception:
        return Response(0)


@api_view(['POST'])
def setCourseVisible(request):
    try:
        course = Entity.objects.get(Q(id=request.data['courseId']))
        course.is_visible = request.data['isVisible']
        course.save()
        return Response(1)
    except Exception:
        return Response(0)

@api_view(['POST'])
def deleteCourseStudent(request):
    try:
        selection = Selection.objects.get(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
    except Exception:
        return Response('Selection Existed', status=status.HTTP_201_CREATED)
    try:
        homeworks = Assignment.objects.filter(Q(course=request.data['courseId']))
        for homework in homeworks:
            execution = Execution.objects.get(Q(user=request.data['userId']) & Q(homework=homework.id))
            execution.delete()
    except Exception:
        return Response('Homework Not Existed', status=status.HTTP_201_CREATED)
    selection.delete()
    return Response(1)


@api_view(['POST'])
def addCourseStudent(request):
    try:
        course = Entity.objects.get(Q(id=request.data['courseId']))
        user = Profile.objects.get(Q(id=request.data['userId']))
    except Exception:
        return Response('user Not Existed', status=status.HTTP_201_CREATED)
    try:
        Selection.objects.get(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
        return Response('Selection Existed', status=status.HTTP_201_CREATED)
    except Exception:
        selection = Selection()
        selection.user = user
        selection.course = course
        selection.select_time = datetime.timedelta(days=30)
        selection.save()
        homeworks = Assignment.objects.filter(Q(course=course.id))
        for homework in homeworks:
            execution = Execution()
            execution.homework = homework
            execution.user = user
            execution.save()
        return Response(1)


@api_view(['POST'])
def addCourseLecture(request):
    try:
        course = Entity.objects.get(Q(id=request.data['courseId']))
        format = Format.objects.get(Q(id=request.data['format']))
    except Exception:
        return Response('Format Not Existed', status=status.HTTP_201_CREATED)
    lecture = Lecture()
    lecture.title = request.data['title']
    lecture.course = course
    lecture.format = format
    lecture.created_time = datetime.timedelta(days=30)
    lecture.save()
    return Response(1)


@api_view(['POST'])
def getCourseByTypeAndPage(request):
    try:
        genre = Genre.objects.get(Q(name=request.data['genre']))
        courses = Entity.objects.filter(Q(is_visible=True) & Q(genre=genre.id))
    except Exception:
        courses = Entity.objects.filter(Q(is_visible=True))
    courses = paginateCourses(request, courses, request.data['pageSize'])
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def getCoursesCount(request):
    try:
        genre = Genre.objects.get(Q(name=request.data['genre']))
        courses = Entity.objects.filter(Q(is_visible=True) & Q(genre=genre.id))
        return Response(len(courses))
    except Exception:
        courses = Entity.objects.filter(Q(is_visible=True))
        return Response(len(courses))


@api_view(['POST'])
def getRecomendedCourse(request):
    userId=request.data['userId']
    if userId:
        courses = Entity.objects.filter(Q(is_visible=True))
    else:
        courses = Entity.objects.filter(Q(is_visible=True))
    serializer = CourseSerializer(courses, many=True)

    courseData = serializer.data[0:request.data['recomendedCoursesCount']]
    return Response(courseData)
