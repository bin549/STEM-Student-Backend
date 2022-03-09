from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assignment, Execution
from .serializers import HomeworkSerializer,ExecutionSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from course.models import Entity, Selection
from users.models import Profile
import datetime, time


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
    new_homework.intro = request.data['intro']
    new_homework.description = request.data['description']
    new_homework.start_time = request.data['start_time']
    new_homework.end_time = request.data['end_time']
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
        userHomework = {'username': user.name, 'finish_time': execution.finish_time,
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
        userHomework = {'id': homework.id, 'description': homework.description,  'intro': homework.intro, 'start_time': homework.start_time,
                         'end_time': homework.end_time, 'score': execution.score,
                         'finish_time': execution.finish_time, 'is_excellent': execution.is_excellent}
        userHomeworks.append(userHomework)
    return Response(userHomeworks)



@api_view(['GET'])
def getExecutionsById(request, homework_id):
    executions = Execution.objects.filter(Q(homework=homework_id))
    n_executions = []
    for execution in executions:
        user = Profile.objects.get(Q(id=execution.user.id))
        n_execution = { 'id': execution.id, 'userName': user.name,
                        'finish_time': execution.finish_time, 'score': execution.score,
                         'is_excellent': execution.is_excellent}
        n_executions.append(n_execution)
    return Response(n_executions)


@api_view(['POST'])
def setExecutionScore(request):
    execution = Execution.objects.get(Q(id=request.data['id']))
    execution.score = request.data['score']
    execution.save()
    return Response(1)


@api_view(['GET'])
def getExecutionExcellentById(request, execution_id):
    execution = Execution.objects.get(Q(id=execution_id))
    execution.is_excellent = True
    execution.save()
    return Response(1)


@api_view(['POST'])
def getCheckedExecutions(request):
    if request.data['is_check'] == False:
        executions = Execution.objects.filter(Q(homework=request.data['id']) & Q(score=None))
    else:
        executions = Execution.objects.filter(Q(homework=request.data['id']))
        executions = executions.exclude(Q(score=None))


    n_executions = []
    for execution in executions:
        user = Profile.objects.get(Q(id=execution.user.id))
        n_execution = { 'id': execution.id, 'userName': user.name,
                        'finish_time': execution.finish_time, 'score': execution.score,
                         'is_excellent': execution.is_excellent}
        n_executions.append(n_execution)
    return Response(n_executions)


@api_view(['GET'])
def getExcellentExecutions(request, homework_id):
    executions = Execution.objects.filter(Q(homework=homework_id) & Q(is_excellent=True))

    n_executions = []
    for execution in executions:
        user = Profile.objects.get(Q(id=execution.user.id))
        n_execution = { 'id': execution.id, 'userName': user.name,
                        'finish_time': execution.finish_time, 'score': execution.score,
                         'is_excellent': execution.is_excellent}
        n_executions.append(n_execution)
    return Response(n_executions)



@api_view(['GET'])
def getExcellentExecutionUserNames(request, homework_id):
    executions = Execution.objects.filter(Q(homework=homework_id) & Q(is_excellent=True))
    userNames = []
    for execution in executions:
        user = Profile.objects.get(Q(id=execution.user.id))
        userNames.append(user.name)
    return Response(userNames)



@api_view(['GET'])
def getHomeworkById(request, homework_id):
    homework = Assignment.objects.get(Q(id=homework_id))
    serializer = HomeworkSerializer(homework, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def uploadHomework(request):
    execution = Execution.objects.get(Q(homework=request.data['homeworkId']) & Q(user=request.data['userId']))
    execution.finish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    execution.save()
    return Response(1)


@api_view(['POST'])
def loadExecution(request):
    execution = Execution.objects.get(Q(homework=request.data['homeworkId']) & Q(user=request.data['userId']))
    serializer = ExecutionSerializer(execution, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def loadCourseAllHomeworks(request):
    executions = Execution.objects.filter(Q(user=request.data['userId']))
    # executions = Execution.objects.filter(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
    homeworks = []
    for execution in executions:
        try:
            homework = Assignment.objects.get(Q(id=execution.homework.id) & Q(course=request.data['courseId']))
            serializer = HomeworkSerializer(homework, many=False)
            homeworks.append(serializer.data)
        except Exception:
            pass
    return Response(homeworks)


@api_view(['GET'])
def getUnfinishHomework(request, user_id):
    executions = Execution.objects.filter(Q(user=user_id) & Q(finish_time=None))
    homeworks = []
    for execution in executions:
        homework = Assignment.objects.get(Q(id=execution.homework.id))
        serializer = HomeworkSerializer(homework, many=False)
        homeworks.append(serializer.data)
    return Response(homeworks)


@api_view(['POST'])
def loadCourseUnfinishHomeworks(request):
    executions = Execution.objects.filter(Q(user=request.data['userId']) & Q(finish_time=None))
    # executions = Execution.objects.filter(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
    homeworks = []
    for execution in executions:
        try:
            homework = Assignment.objects.get(Q(id=execution.homework.id) & Q(course=request.data['courseId']))
            serializer = HomeworkSerializer(homework, many=False)
            homeworks.append(serializer.data)
        except Exception:
            pass
    return Response(homeworks)
