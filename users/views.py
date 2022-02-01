from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import UserSerializer
from rest_framework.decorators import api_view


class AllUsers(APIView):

    def get(self, request, format=None):
        profiles = Profile.objects.all()[0:4]
        serializer = UserSerializer(profiles, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getUserInfo(request, pk):
    profile = Profile.objects.get(name=pk)
    serializer = UserSerializer(profile, many=False)
    return Response(serializer.data)
