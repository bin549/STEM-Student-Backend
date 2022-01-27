from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import UserSerializer


class AllUsers(APIView):

    def get(self, request, format=None):
        profiles = Profile.objects.all()[0:4]
        serializer = UserSerializer(profiles, many=True)
        return Response(serializer.data)
