from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Type
from .serializers import UserSerializer, TypeSerializer
from rest_framework.decorators import api_view
from rest_framework import status


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


@api_view(['POST'])
def getUserTypeName(request):
    type = Type.objects.get(id=request.data['userTypeId'])
    serializer = TypeSerializer(type, many=False)
    return Response(serializer.data['name'])


@api_view(['GET'])
def getUsersByTypeName(request, type_name):
    try:
        user_type = Type.objects.get(name=type_name)
    except Exception:
        return Response('user Type Not Existed', status=status.HTTP_201_CREATED)
    users = Profile.objects.filter(user_type=user_type.id)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    print(request.data)
    return Response(1)
