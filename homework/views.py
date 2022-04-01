from .serializers import HomeworkSerializer, ExecutionSerializer, MediaSerializer, MediaTypeSerializer
import datetime
import time
from django.core.files.storage import default_storage
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from course.models import Entity, Selection
from users.models import Profile
from .models import Assignment, Execution, MediaType, Media, ExecutionStar


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
def loadUserExecution(request):
    userId = request.data['userId']
    homeworkId = request.data['homeworkId']
    execution = Execution.objects.get(Q(homework=homework.id) & Q(user=userId))
    serializer = ExecutionSerializer(execution, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getExecutionsById(request, homework_id):
    executions = Execution.objects.filter(Q(homework=homework_id))
    n_executions = []
    for execution in executions:
        user = Profile.objects.get(Q(id=execution.user.id))
        n_execution = {'id': execution.id, 'userName': user.name,
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
        executions = Execution.objects.filter(
            Q(homework=request.data['id']) & Q(score=None))
    else:
        executions = Execution.objects.filter(Q(homework=request.data['id']))
        executions = executions.exclude(Q(score=None))
    n_executions = []
    for execution in executions:
        user = Profile.objects.get(Q(id=execution.user.id))
        n_execution = {'id': execution.id, 'userName': user.name,
                       'finish_time': execution.finish_time, 'score': execution.score,
                       'is_excellent': execution.is_excellent}
        n_executions.append(n_execution)
    return Response(n_executions)


@api_view(['GET'])
def getExcellentExecutions(request, homework_id):
    executions = Execution.objects.filter(
        Q(homework=homework_id) & Q(is_excellent=True))
    n_executions = []
    for execution in executions:
        user = Profile.objects.get(Q(id=execution.user.id))
        n_execution = {'id': execution.id, 'userName': user.name,
                       'finish_time': execution.finish_time, 'score': execution.score,
                       'is_excellent': execution.is_excellent}
        n_executions.append(n_execution)
    return Response(n_executions)


@api_view(['GET'])
def loadExcellentExecutions(request):
    executions = Execution.objects.filter(Q(is_excellent=True))
    n_executions = []
    for execution in executions:
        user = Profile.objects.get(Q(id=execution.user.id))
        content_images = []
        media_type = MediaType.objects.get(Q(name="Photo"))
        medias = Media.objects.filter(
            Q(execution=execution.id) & Q(type=media_type))
        for media in medias:
            content_images.append(media.get_media())
        n_execution = {'id': execution.id,
                       'user_id': user.user_id,
                       'user_name': user.name,
                       'user_image': user.get_image(),
                       'user_id': user.id,
                       'finish_time': execution.finish_time,
                       'content_text': execution.content_text,
                       'content_images': content_images
                       }
        n_executions.append(n_execution)
    return Response(n_executions)


@api_view(['GET'])
def getExcellentExecutionUserNames(request, homework_id):
    executions = Execution.objects.filter(
        Q(homework=homework_id) & Q(is_excellent=True))
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


@api_view(['GET'])
def getHomeworks(request, user_id):
    executions = Execution.objects.filter(Q(user=user_id))
    homeworks = []
    for execution in executions:
        homework = {"id": execution.homework.id, "intro": execution.homework.intro, "description": execution.homework.description[0:50]+"...", 'finish_time': execution.finish_time
                    }
        homeworks.append(homework)
    return Response(homeworks)
    # homework = Assignment.objects.filter(Q(id=homework_id))
    # serializer = HomeworkSerializer(homework, many=False)
    # return Response(serializer.data)


@api_view(['POST'])
def uploadHomework(request):
    execution = Execution.objects.get(
        Q(homework=request.data['homeworkId']) & Q(user=request.data['userId']))
    execution.finish_time = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime())
    execution.content_text = request.data['contentText']
    photo_format = ('png', 'jpg', 'jpeg', 'bmp', 'gif')
    video_format = ('mp4', 'mov')
    for contentMedia in request.data['contentMedia']:
        media = Media()
        if contentMedia.split('.')[-1].lower() in photo_format:
            media_type = MediaType.objects.get(Q(name='Photo'))
        elif contentMedia.split('.')[-1].lower() in video_format:
            media_type = MediaType.objects.get(Q(name='Video'))
        media.media = contentMedia
        media.execution = execution
        media.type = media_type
        media.save()
    execution.save()
    return Response(1)


@api_view(['POST'])
def loadExecution(request):
    execution = Execution.objects.get(
        Q(homework=request.data['homeworkId']) & Q(user=request.data['userId']))
    serializer = ExecutionSerializer(execution, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getExecutionImages(request, execution_id):
    execution = Execution.objects.get(Q(id=execution_id))
    media_type = MediaType.objects.get(Q(name="Photo"))
    medias = Media.objects.filter(
        Q(execution=execution.id) & Q(type=media_type))
    serializer = MediaSerializer(medias, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def loadHomeworks(request):
    userId = request.data['userId']
    courseId = request.data['courseId']
    homeworks = Assignment.objects.filter(Q(course=courseId))
    userHomeworks = []
    for homework in homeworks:
        execution = Execution.objects.get(
            Q(homework=homework.id) & Q(user=userId))
        userHomework = {'id': homework.id, 'description': homework.description,  'intro': homework.intro, 'start_time': homework.start_time,
                        'end_time': homework.end_time, 'score': execution.score,
                        'finish_time': execution.finish_time, 'is_excellent': execution.is_excellent}
        userHomeworks.append(userHomework)
    return Response(userHomeworks)


@api_view(['POST'])
def loadCourseAllHomeworks(request):
    executions = Execution.objects.filter(Q(user=request.data['userId']))
    # executions = Execution.objects.filter(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
    userHomeworks = []
    for execution in executions:
        try:
            homework = Assignment.objects.get(
                Q(id=execution.homework.id) & Q(course=request.data['courseId']))
            userHomework = {'id': homework.id, 'description': homework.description[0:50]+"...",  'intro': homework.intro, 'start_time': homework.start_time,
                            'end_time': homework.end_time, 'score': execution.score,
                            'finish_time': execution.finish_time, 'is_excellent': execution.is_excellent}
            userHomeworks.append(userHomework)
        except Exception:
            pass
    return Response(userHomeworks)


@api_view(['POST'])
def loadCourseHomeworks(request):
    if (request.data['is_finish']):
        executions = Execution.objects.filter(Q(user=request.data['userId']))
        executions = executions.exclude(Q(finish_time=None))
    else:
        executions = Execution.objects.filter(
            Q(user=request.data['userId']) & Q(finish_time=None))
    userHomeworks = []
    for execution in executions:
        try:
            if (request.data['courseId'] != 0):
                homework = Assignment.objects.get(
                    Q(id=execution.homework.id) & Q(course=request.data['courseId']))
            else:
                homework = Assignment.objects.get(Q(id=execution.homework.id))
            userHomework = {"id": execution.homework.id, "intro": execution.homework.intro, "description": execution.homework.description[0:50]+"...",
                            'finish_time': execution.finish_time}
            userHomeworks.append(userHomework)
        except Exception:
            pass
    return Response(userHomeworks)


@api_view(['POST'])
def loadCourseUnfinishHomeworks(request):
    executions = Execution.objects.filter(
        Q(user=request.data['userId']) & Q(finish_time=None))
    # executions = Execution.objects.filter(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
    userHomeworks = []
    for execution in executions:
        try:
            homework = Assignment.objects.get(
                Q(id=execution.homework.id) & Q(course=request.data['courseId']))
            userHomework = {'id': homework.id, 'description': homework.description,  'intro': homework.intro, 'start_time': homework.start_time,
                            'end_time': homework.end_time, 'score': execution.score,
                            'finish_time': execution.finish_time, 'is_excellent': execution.is_excellent}
            userHomeworks.append(userHomework)
        except Exception:
            pass
    return Response(userHomeworks)


@api_view(['POST'])
def loadCourseFinishHomeworks(request):
    executions = Execution.objects.filter(Q(user=request.data['userId']))
    executions = executions.exclude(Q(finish_time=None))
    # executions = Execution.objects.filter(Q(user=request.data['userId']) & Q(course=request.data['courseId']))
    userHomeworks = []
    for execution in executions:
        try:
            homework = Assignment.objects.get(
                Q(id=execution.homework.id) & Q(course=request.data['courseId']))
            userHomework = {'id': homework.id, 'description': homework.description,  'intro': homework.intro, 'start_time': homework.start_time,
                            'end_time': homework.end_time, 'score': execution.score,
                            'finish_time': execution.finish_time, 'is_excellent': execution.is_excellent}
            userHomeworks.append(userHomework)
        except Exception:
            pass
    return Response(userHomeworks)


@api_view(['GET'])
def getUnfinishHomework(request, user_id):
    executions = Execution.objects.filter(
        Q(user=user_id) & Q(finish_time=None))
    homeworks = []
    for execution in executions:
        homework = Assignment.objects.get(Q(id=execution.homework.id))
        serializer = HomeworkSerializer(homework, many=False)
        homeworks.append(serializer.data)
    return Response(homeworks)


@api_view(['POST'])
def getStarStatus(request):
    try:
        executionStar = ExecutionStar.objects.get(
            Q(user=request.data['user_id']) & Q(execution=request.data['execution_id']))
        return Response(1)
    except Exception:
        return Response(0)


@api_view(['POST'])
def changeStarStatus(request):
    if request.data["star_status"]:
        star = ExecutionStar()
        user = Profile.objects.get(Q(id=request.data['user_id']))
        execution = Execution.objects.get(Q(id=request.data['execution_id']))
        star.user = user
        star.execution = execution
        star.star_time = datetime.timedelta(days=30)
        star.save()
        return Response(1)
    else:
        star = ExecutionStar.objects.get(Q(user=request.data['user_id']) & Q(
            execution=request.data['execution_id']))
        star.delete()
    return Response(0)


@api_view(['GET'])
def getUserStarExecutions(request, user_id):
    stars = ExecutionStar.objects.filter(Q(user=user_id))
    executions = []
    for star in stars:
        execution = Execution.objects.get(Q(id=star.execution.id))
        user = Profile.objects.get(Q(id=execution.user.id))
        content_images = []
        media_type = MediaType.objects.get(Q(name="Photo"))
        medias = Media.objects.filter(
            Q(execution=execution.id) & Q(type=media_type))
        for media in medias:
            content_images.append(media.get_media())
        n_execution = {'id': execution.id,
                       'user_name': user.name,
                       'user_image': user.get_image(),
                       'user_id': user.id,
                       'finish_time': execution.finish_time,
                       'content_text': execution.content_text,
                       'content_images': content_images
                       }
        executions.append(n_execution)
    return Response(executions)


@api_view(['POST'])
def removeStar(request):
    try:
        star = ExecutionStar.objects.get(Q(user=request.data['user_id']) & Q(
            execution=request.data['execution_id']))
        star.delete()
        return Response(1)
    except Exception:
        return Response(0)


@api_view(['GET'])
def getCourseId(request, homework_id):
    homework = Assignment.objects.get(Q(id=homework_id))
    return Response(homework.course.id)


@api_view(['GET'])
def getHomeworkId(request, execution_id):
    execution = Execution.objects.get(Q(id=execution_id))
    return Response(execution.homework.id)


@api_view(['GET'])
def getExecutionById(request, execution_id):
    execution = Execution.objects.get(Q(id=execution_id))
    content_images = []
    media_type = MediaType.objects.get(Q(name="Photo"))
    medias = Media.objects.filter(
        Q(execution=execution.id) & Q(type=media_type))
    for media in medias:
        content_images.append(media.get_media())
    n_execution = {'id': execution.id,
                   'finish_time': execution.finish_time,
                   'content_text': execution.content_text,
                   'is_excellent': execution.is_excellent,
                   'content_images': content_images
                   }
    return Response(n_execution)
