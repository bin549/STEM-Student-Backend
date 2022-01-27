from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assignment
from .serializers import HomeworkSerializer


class AllHomework(APIView):

    def get(self, request, format=None):
        homeworks = Homework.objects.all()[0:4]
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)
