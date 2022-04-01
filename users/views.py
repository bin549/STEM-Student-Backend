import datetime
from .models import Profile, Type, Message, Follow
from .serializers import UserSerializer, TypeSerializer, MessageSerializer
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


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
def getUserInfoById(request, user_id):
    profile = Profile.objects.get(id=user_id)
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


@api_view(['POST'])
def getFollowStatus(request):
    try:
        follow = Follow.objects.get(Q(user=request.data['user_id']) & Q(other_user=request.data['other_user_id']))
        return Response(1)
    except Exception:
        return Response(0)


@api_view(['POST'])
def addFollow(request):
    try:
        follow = Follow.objects.get(Q(user=request.data['user_id']) & Q(other_user=request.data['other_user_id']))
        return Response(0)
    except Exception:
        new_follow = Follow()
        user = Profile.objects.get(Q(id=request.data['user_id']))
        other_user = Profile.objects.get(Q(id=request.data['other_user_id']))
        new_follow.user = user
        new_follow.other_user = other_user
        new_follow.follow_time = datetime.timedelta(days=30)
        new_follow.save()
        return Response(1)


@api_view(['POST'])
def removeFollow(request):
    try:
        follow = Follow.objects.get(Q(user=request.data['user_id']) & Q(other_user=request.data['other_user_id']))
        follow.delete()
        return Response(1)
    except Exception:
        return Response(0)


@api_view(['GET'])
def getFollowersId(request, user_id):
    follows = Follow.objects.filter(other_user=user_id)
    followers = []
    for follow in follows:
        follower = Profile.objects.get(Q(id=follow.other_user.id))
        followers.append(
            {
                "id": follower.id
            }
        )
    return Response(followers)


@api_view(['GET'])
def getFollowingsId(request, user_id):
    follows = Follow.objects.filter(user=user_id)
    followers = []
    for follow in follows:
        follower = Profile.objects.get(Q(id=follow.other_user.id))
        followers.append(
            {
                "id": follower.id
            }
        )
    return Response(followers)
