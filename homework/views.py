from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assignment
from .serializers import HomeworkSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from course.models import Entity
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
    try:
        course = Entity.objects.get(Q(id=request.data['courseId']))
    except Exception:
        return Response(0)
    new_homework = Assignment()
    new_homework.start_time = datetime.timedelta(days=30)
    new_homework.end_time = datetime.timedelta(days=30)
    new_homework.intro = request.data['intro']
    new_homework.course = course
    new_homework.save()
    return Response(1)
