import datetime
import random
from django.core.files.storage import default_storage
from django.http import Http404
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from homework.models import Assignment, Execution
from users.models import Profile
from users.serializers import UserSerializer
from .models import Entity, Genre, Selection, Wishlist, Lecture, Format, Comment, History, Progress
from .serializers import CourseSerializer, GenreSerializer, SelectionSerializer, WishlistSerializer, LectureSerializer, FormatSerializer, CommentSerializer, HistorySerializer
from .utils import paginateCourses


class CourseAPI(APIView):

    def get(self, request, course_name, format=None):
        course = Entity.objects.get(title=course_name)
        serializer = CourseSerializer(course, many=False)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.data["mode"] == "user":
            selections = Selection.objects.filter(Q(user=request.data["user_id"]))
            course_ids = set()
            for e in selections:
                course_ids.add(e.course.id)
            try:
                genre = Genre.objects.get(Q(name=request.data['genre']))
                courses = Entity.objects.filter(Q(genre=genre.id) & Q(id__in=course_ids))
            except Exception:
                courses = Entity.objects.filter(Q(id__in=course_ids))
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        elif request.data["mode"] == "count":
            if "user_id" in request.data:
                selections = Selection.objects.filter(Q(user=request.data['user_id']))
                course_ids = set()
                for e in selections:
                    course_ids.add(e.course.id)
                try:
                    genre = Genre.objects.get(Q(name=request.data['genre']))
                    courses = Entity.objects.filter(Q(genre=genre.id) & Q(id__in=course_ids))
                except Exception:
                    courses = Entity.objects.filter(Q(id__in=course_ids))
                return Response(len(courses))
            else:
                try:
                    genre = Genre.objects.get(Q(name=request.data['genre']))
                    courses = Entity.objects.filter(Q(is_visible=True) & Q(genre=genre.id))
                    return Response(len(courses))
                except Exception:
                    courses = Entity.objects.filter(Q(is_visible=True))
                    return Response(len(courses))
        elif request.data["mode"] == "progress":
            selection = Selection.objects.get(Q(course=request.data["course_id"]) & Q(user=request.data["user_id"]))
            all_lectures = Lecture.objects.filter(Q(course=selection.course.id))
            checked_lectures = Progress.objects.filter(Q(user=request.data["user_id"]) & Q(percent=1.0))
            left_lectures = checked_lectures.filter(Q(lecture__in=all_lectures))
            return Response(float(len(left_lectures)) / (len(all_lectures)))
        elif request.data["mode"] == "condition":
            try:
                genre = Genre.objects.get(Q(name=request.data['genre']))
                courses = Entity.objects.filter(Q(is_visible=True) & Q(genre=genre.id))
            except Exception:
                courses = Entity.objects.filter(Q(is_visible=True))
            courses = paginateCourses(request, courses, request.data['pageSize'])
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        elif request.data["mode"] == "recommend":
            if "user_id" in request.data:
                course_ids = set()
                selections = Selection.objects.filter(Q(user=request.data["user_id"]))
                wishlists = Wishlist.objects.filter(Q(user=request.data["user_id"]))
                for e in selections:
                    course_ids.add(e.course.id)
                for e in wishlists:
                    course_ids.add(e.course.id)
                courses = Entity.objects.exclude(Q(id__in=course_ids))
                courses = courses.filter(Q(is_visible=True))
            else:
                courses = Entity.objects.filter(Q(is_visible=True))
            serializer = CourseSerializer(courses, many=True)
            courseData = serializer.data
            random.shuffle(courseData)
            return Response(courseData[0:request.data['recomendedCoursesCount']])
        elif request.data["mode"] == "homework":
            selections = Selection.objects.filter(Q(user=request.data['user_id']))
            courses = []
            for selection in selections:
                course = Entity.objects.get(Q(id=selection.course.id))
                courses.append(course)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)



class LectureAPI(APIView):

    def get(self, request, course_id, format=None):
        lectures = Lecture.objects.filter(Q(course=course_id)).order_by("index")
        serializer = LectureSerializer(lectures, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if "mode" in request.data:
            if request.data["mode"] == "preview":
                lectures = Lecture.objects.filter(Q(course=request.data["course_id"])).order_by("index")
                lecture = lectures.get(Q(is_preview=True))
                serializer = LectureSerializer(lecture, many=False)
                return Response(serializer.data)
        elif "lecture_id" in request.data:
            lecture = Lecture.objects.get(Q(id=request.data["lecture_id"]))
            serializer = LectureSerializer(lecture, many=False)
            return Response(serializer.data)


class FormatAPI(APIView):

    def get(self, request, format=None):
        formats = Format.objects.all()
        serializer = FormatSerializer(formats, many=True)
        return Response(serializer.data)


class SelectionAPI(APIView):

    def post(self, request, format=None):
        if "serial_number" in request.data:
            try:
                user = Profile.objects.get(Q(id=request.data['user_id']))
                course = Entity.objects.get(Q(serial_number=request.data['serial_number']))
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
                lectures = Lecture.objects.filter(course=course.id)
                for lecture in lectures:
                    progress = Progress()
                    progress.user = user
                    progress.lecture = lecture
                    progress.percent = 0.0
                    progress.save()
            return Response('Register Success.')
        else:
            try:
                selection = Selection.objects.get(Q(user=request.data['user_id']) & Q(course=request.data['course_id']))
                return Response(1)
            except Exception:
                return Response(0)


class CommentAPI(APIView):

    def get(self, request, lecture_id, format=None):
        comments = Comment.objects.filter(Q(lecture=lecture_id))
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if "mode" in request.data:
            if request.data["mode"] == "create":
                user = Profile.objects.get(Q(id=request.data['user_id']))
                lecture = Lecture.objects.get(Q(id=request.data['lecture_id']))
                if lecture.is_comment_check:
                    lecture.is_comment_check = False
                    lecture.save()
                comment = Comment()
                comment.user = user
                comment.lecture = lecture
                comment.content = request.data['content']
                comment.comment_time = datetime.timedelta(days=30)
                comment.save()
                return Response('createCourse!')
            if request.data["mode"] == "delete":
                comment = Comment.objects.get(Q(id=request.data["comment_id"]))
                comment.delete()
                return Response(1)
        if "user_id" in request.data:
            comments = Comment.objects.filter(Q(user=request.data["user_id"]))
            n_comments = []
            for comment in comments:
                lecture = Lecture.objects.get(Q(id=comment.lecture.id))
                n_comment = {'id': comment.id, 'lecture': lecture.title, 'content': comment.content,
                             'comment_time': comment.comment_time}
                n_comments.append(n_comment)
            return Response(n_comments)



@api_view(['GET'])
def getUserWishlist(request, user_id):
    collections = Wishlist.objects.filter(Q(user=user_id))
    courses = []
    for c in collections:
        course = Entity.objects.get(Q(id=c.course.id))
        courses.append(course)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)



class WishlistAPI(APIView):

    def get(self, request, user_id, format=None):
        wishlists = Wishlist.objects.filter(Q(user=user_id))
        courses = []
        for wishlist in wishlists:
            courses.append(wishlist.course)
            serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.data["mode"] == "fetch":
            try:
                wishlist = Wishlist.objects.get(Q(user=request.data['user_id']) & Q(course=request.data['course_id']))
                return Response(1)
            except Exception:
                return Response(0)
        elif request.data["mode"] == "create":
            wishlist = Wishlist()
            user = Profile.objects.get(Q(id=request.data['userId']))
            course = Entity.objects.get(Q(id=request.data['courseId']))
            wishlist.user = user
            wishlist.course = course
            wishlist.collect_time = datetime.timedelta(days=30)
            wishlist.save()
        elif request.data["mode"] == "delete":
            wishlist = Wishlist.objects.get(Q(user=request.data['user_id']) & Q(course=request.data['course_id']))
            wishlist.delete()
            return Response(1)

    def delete(self, request, format=None):
        return Response(1)


class GenreAPI(APIView):

    def get(self, request, format=None):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def getCourseGenre(request, genre_id):
    genre = Genre.objects.get(Q(id=genre_id))
    serializer = GenreSerializer(genre, many=False)
    return Response(serializer.data)


class ProgressAPI(APIView):

    def post(self, request, format=None):
        course = Entity.objects.get(Q(id=request.data["course_id"]))
        lectures = Lecture.objects.filter(Q(course=course.id))
        data = {}
        for lecture in lectures:
            progress = Progress.objects.get(Q(lecture=lecture.id) & Q(user=request.data["user_id"]))
            data[str(lecture.id)] = progress.percent==1.0
        return Response(data)

    def put(self, request, forsmat=None):
        progress = Progress.objects.get(Q(user=request.data["user_id"]) & Q(lecture=request.data["lecture_id"]))
        progress.percent = 1.0
        progress.save()
        # genres = Genre.objects.all()[0:4]
        # serializer = GenreSerializer(genres, many=True)
        return Response(1)




class AllVisibleCourse(APIView):

    def get(self, request, format=None):
        courses = Entity.objects.filter(Q(is_visible=True))
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


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
def getCourseOwner(request, course_id):
    course = Entity.objects.get(Q(id=course_id))
    owner = Profile.objects.get(id=course.owner.id)
    serializer = UserSerializer(owner, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getCourse(request, course_id):
    courses = Entity.objects.get(Q(id=course_id))
    serializer = CourseSerializer(courses, many=False)
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




class HistoryAPI(APIView):

    def get(self, request, user_id, format=None):
        histories = History.objects.filter(user=user_id).order_by("-learn_time")[0:50]
        datas = []
        for history in histories:
            print(history.learn_time)
            lecture = Lecture.objects.get(Q(id=history.lecture.id))
            course = Entity.objects.get(Q(id=lecture.course.id))
            data = {
                "lecture": lecture.title,
                "course": course.title,
                "learn_time": history.learn_time,
            }
            datas.append(data)
        return Response(datas)

    def post(self, request, format=None):
        history = History()
        user = Profile.objects.get(Q(id=request.data["user_id"]))
        lecture = Lecture.objects.get(Q(id=request.data["lecture_id"]))
        history.user = user
        history.lecture = lecture
        history.learn_time = datetime.timedelta(days=30)
        history.save()
        return Response(1)

    def delete(self, request, history_id, format=None):
        history = History.objects.get(Q(id=history_id))
        history.delete()
        return Response(1)


@api_view(['POST'])
def getCourseVisibleStatus(request):
    try:
        course = Entity.objects.get(Q(id=request.data['courseId']))
        if course.is_visible:
            return Response(1)
        return Response(0)
    except Exception:
        return Response(0)

@api_view(['GET'])
def getLectureFormat(request, format_id):
    format = Format.objects.get(Q(id=format_id))
    serializer = FormatSerializer(format, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def loadCurrentSelectCourseTitle(request, course_id):
    course = Entity.objects.get(Q(id=course_id))
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)
