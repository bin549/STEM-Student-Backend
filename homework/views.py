from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assignment, Execution
from .serializers import HomeworkSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from course.models import Entity, Selection
from users.models import Profile
import datetime


class AllHomework(APIView):

    def get(self, request, format=None):
        homeworks = Homework.objects.all()[0:4]
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getSelectedCourseHomeworks(request, course_id):
    homeworks = Assignment.objects.filter(Q(course=course_id))
    serializer = HomeworkSerializer(homeworks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addHomework(request):
    courseId = request.data['courseId']
    try:
        course = Entity.objects.get(Q(id=courseId))
    except Exception:
        return Response(0)
    new_homework = Assignment()
    new_homework.start_time = datetime.timedelta(days=30)
    new_homework.end_time = datetime.timedelta(days=30)
    new_homework.intro = request.data['intro']
    new_homework.course = course
    new_homework.save()

    selections = Selection.objects.filter(Q(course=courseId))
    for selection in selections:
        execution = Execution()
        execution.homework = new_homework
        execution.user = selection.user
        execution.save()
    return Response(1)


@api_view(['POST'])
def deleteHomework(request):
    homeworkId = request.data['homeworkId']
    try:
        homework = Assignment.objects.get(Q(id=homeworkId))
        homework.delete()
        executions = Execution.objects.filter(Q(homework=homeworkId))
        for execution in executions:
            execution.delete()
        return Response(1)
    except Exception:
        return Response(0)


@api_view(['POST'])
def loadExecution(request):
    homeworkId = request.data['homeworkId']
    executions = Execution.objects.filter(Q(homework=homeworkId))
    userHomeworks = []
    for execution in executions:
        user = Profile.objects.get(Q(id=homework.user))
        userHomework = {'username': user.name, 'is_finish': execution.is_finish,
                        'is_excellent': execution.is_excellent, 'score': execution.score}
        userHomeworks.append(userHomework)
    return Response(1)


@api_view(['POST'])
def loadHomeworks(request):
    userId = request.data['userId']
    courseId = request.data['courseId']
    homeworks = Assignment.objects.filter(Q(course=courseId))

    userHomeworks = []
    for homework in homeworks:
        execution = Execution.objects.get(Q(homework=homework.id) & Q(user=userId))
        userHomework = {'intro': homework.intro, 'start_time': homework.start_time, 'end_time': homework.end_time, 'score': execution.score, 'is_finish': execution.is_finish, 'is_excellent': execution.is_excellent}
        userHomeworks.append(userHomework)

    return Response(userHomeworks)
