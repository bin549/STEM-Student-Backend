from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Type, Message
from .serializers import UserSerializer, TypeSerializer, MessageSerializer
from rest_framework.decorators import api_view
from rest_framework import status
import datetime
from django.db.models import Q


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


@api_view(['GET'])
def getUserById(request, user_id):
    profile = Profile.objects.get(id=user_id)
    serializer = UserSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUserNameById(request, user_id):
    profile = Profile.objects.get(id=user_id)
    serializer = UserSerializer(profile, many=False)
    return Response(serializer.data['name'])


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


@api_view(['POST'])
def updateUser(request):
    user = Profile.objects.get(id=request.data['userId'])
    user.profile_image = request.data['profile_image']
    user.save()
    return Response(1)

@api_view(['POST'])
def createMessage(request):
    message = Message()
    message.sender = Profile.objects.get(id=request.data['sender'])
    message.title = request.data['title']
    message.content = request.data['content']
    message.is_read = False
    message.created_time = datetime.timedelta(days=30)
    user_type = Type.objects.get(name='manager')
    recipients = Profile.objects.filter(user_type=user_type.id)
    for recipient in recipients:
        message.recipient = recipient
        message.save()
    return Response(1)


@api_view(['POST'])
def getInboxUnreadCount(request):
    user = Profile.objects.get(name=request.data['user'])
    messages = Message.objects.filter(Q(recipient=user.id) & Q(is_read=False))
    return Response(messages.count())


@api_view(['POST'])
def getInboxReadCount(request):
    user = Profile.objects.get(name=request.data['user'])
    messages = Message.objects.filter(Q(recipient=user.id) & Q(is_read=True))
    return Response(messages.count())


@api_view(['POST'])
def getMessages(request):
    user = Profile.objects.get(name=request.data['user'])
    if request.data['is_read'] == None:
        messages = Message.objects.filter(recipient=user.id)
    else:
        if request.data['is_read'] == False:
            messages = Message.objects.filter(Q(recipient=user.id) & Q(is_read=False))
        else:
            messages = Message.objects.filter(Q(recipient=user.id) & Q(is_read=True))
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMessage(request, message_id):
    message = Message.objects.get(id=message_id)
    serializer = MessageSerializer(message, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def SetMessageIsReadStatus(request, message_id):
    message = Message.objects.get(id=message_id)
    if message.is_read == False:
        message.is_read = True
        message.save()
    return Response(1)


@api_view(['GET'])
def deleteMessage(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return Response(1)
