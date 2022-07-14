import datetime
import time
from .serializers import HomeworkSerializer, ExecutionSerializer, MediaSerializer, MediaTypeSerializer
from django.core.files.storage import default_storage
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from course.models import Entity, Selection
from users.models import Profile
from .models import Assignment, Execution, MediaType, Media, ExecutionStar, Log, LogType


class AssignmentAPI(APIView):

    def get(self, request, format=None):
        if request.query_params.__contains__("homework_id"):
            homework = Assignment.objects.get(Q(id=request.query_params["homework_id"]))
            serializer = HomeworkSerializer(homework, many=False)
            return Response(serializer.data)
        elif request.query_params.__contains__("is_finish"):
            if request.query_params["is_finish"]:
                executions = Execution.objects.filter(Q(user=request.query_params['user_id']))
                executions = executions.exclude(Q(finish_time=None))
            else:
                executions = Execution.objects.filter(Q(user=request.query_params['user_id']) & Q(finish_time=None))
            userHomeworks = []
            for execution in executions:
                try:
                    if request.query_params['course_id'] != 0:
                        homework = Assignment.objects.get(Q(id=execution.homework.id) & Q(course=request.query_params['course_id']))
                    else:
                        homework = Assignment.objects.get(Q(id=execution.homework.id))
                    userHomework = {"id": execution.homework.id, "intro": execution.homework.intro, "description": execution.homework.description[0:50]+"...",
                                    'finish_time': execution.finish_time}
                    userHomeworks.append(userHomework)
                except Exception:
                    pass
            return Response(userHomeworks)
        elif request.query_params.__contains__("course_id"):
            executions = Execution.objects.filter(Q(user=request.query_params['user_id']))
            userHomeworks = []
            for execution in executions:
                try:
                    homework = Assignment.objects.get(Q(id=execution.homework.id) & Q(course=request.query_params['course_id']))
                    userHomework = {'id': homework.id, 'description': homework.description[0:50]+"...",  'intro': homework.intro, 'start_time': homework.start_time,
                                    'end_time': homework.end_time, 'finish_time': execution.finish_time, 'is_excellent': execution.is_excellent}
                    userHomeworks.append(userHomework)
                except Exception:
                    pass
            return Response(userHomeworks)
        else:
            executions = Execution.objects.filter(Q(user=request.query_params["user_id"]))
            homeworks = []
            for execution in executions:
                homework = {"id": execution.homework.id, "intro": execution.homework.intro, "description": execution.homework.description[0:350]+"...", 'finish_time': execution.finish_time, "appraise_text": execution.appraise_text}
                homeworks.append(homework)
            return Response(homeworks)


class MediaAPI(APIView):

    def get(self, request, format=None):
        execution = Execution.objects.get(Q(id=request.query_params["execution_id"]))
        media_type = MediaType.objects.get(Q(name="Photo"))
        medias = Media.objects.filter(Q(execution=execution.id) & Q(type=media_type))
        serializer = MediaSerializer(medias, many=True)
        return Response(serializer.data)


class StarAPI(APIView):

    def get(self, request, format=None):
        if request.query_params.__contains__("execution_id"):
            try:
                ExecutionStar.objects.get(Q(user=request.query_params['user_id']) & Q(execution=request.query_params['execution_id']))
                return Response(1)
            except Exception:
                return Response(0)
        else:
            stars = ExecutionStar.objects.filter(Q(user=request.query_params['user_id']))
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
                n_execution = {
                                'id': execution.id,
                               'user_name': user.name,
                               'user_image': user.get_image(),
                               'user_id': user.id,
                               'finish_time': execution.finish_time,
                               'content_text': execution.content_text,
                               'content_images': content_images
                               }
                executions.append(n_execution)
            return Response(executions)

    def post(self, request, format=None):
        star = ExecutionStar()
        user = Profile.objects.get(Q(id=request.data['user_id']))
        execution = Execution.objects.get(Q(id=request.data['execution_id']))
        star.user = user
        star.execution = execution
        star.star_time = datetime.timedelta(days=30)
        star.save()
        return Response(1)

    def delete(self, request, format=None):
        star = ExecutionStar.objects.get(Q(user=request.data['user_id']) & Q(execution=request.data['execution_id']))
        star.delete()
        return Response(1)


class ExecutionAPI(APIView):

    def get(self, request, format=None):
        if request.query_params.__contains__("is_excellent"):
            executions = Execution.objects.filter(Q(is_excellent=True))
            n_executions = []
            for execution in executions:
                user = Profile.objects.get(Q(id=execution.user.id))
                content_images = []
                media_type = MediaType.objects.get(Q(name="Photo"))
                medias = Media.objects.filter(Q(execution=execution.id) & Q(type=media_type))
                for media in medias:
                    content_images.append(media.get_media())
                n_execution = {
                               'id': execution.id,
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
        else:
            execution = Execution.objects.get(Q(homework=request.query_params['homework_id']) & Q(user=request.query_params['user_id']))
            serializer = ExecutionSerializer(execution, many=False)
            return Response(serializer.data)

    def put(self, request, format=None):
        execution = Execution.objects.get(Q(homework=request.data['homework_id']) & Q(user=request.data['user_id']))
        execution.finish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        execution.content_text = request.data['content_text']
        photo_format = ('png', 'jpg', 'jpeg', 'bmp', 'gif')
        video_format = ('mp4', 'mov')
        for content_media in request.data['content_medias']:
            media = Media()
            if content_media.split('.')[-1].lower() in photo_format:
                media_type = MediaType.objects.get(Q(name='Photo'))
            elif content_media.split('.')[-1].lower() in video_format:
                media_type = MediaType.objects.get(Q(name='Video'))
            media.media = content_media
            media.execution = execution
            media.type = media_type
            media.save()
        execution.save()
        return Response(1)


class LogAPI(APIView):

    def post(self, request, format=None):
        log = Log()
        execution = Execution.objects.get(Q(id=request.data["execution_id"]))
        log_type = LogType.objects.get(Q(name="提交"))
        log.execution = execution
        log.log_type = log_type
        log.log_time = datetime.timedelta(days=30)
        log.save()
        return Response(1)
