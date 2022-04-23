import datetime
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Type, Message, Follow, Note
from .serializers import UserSerializer, TypeSerializer, MessageSerializer, NoteSerializer



class ProfileAPI(APIView):

    def get(self, request, user_id,format=None):
        profile = Profile.objects.get(id=user_id)
        serializer = UserSerializer(profile, many=False)
        return Response(serializer.data)



class FollowAPI(APIView):

    def post(self, request, format=None):
        try:
            follow = Follow.objects.get(Q(user=request.data['user_id']) & Q(other_user=request.data['other_user_id']))
            return Response(1)
        except Exception:
            return Response(0)



class NoteAPI(APIView):

    def get(self, request, user_id,format=None):
        notes = Note.objects.filter(user=user_id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        note = Note.objects.get(id=request.data["note_id"])
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)



@api_view(['GET'])
def getUserByUserName(request, pk):
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


@api_view(['GET'])
def getInboxUnreadCount(request, user_name):
    user = Profile.objects.get(name=user_name)
    messages = Message.objects.filter(Q(recipient=user.id) & Q(is_read=False))
    return Response(messages.count())


@api_view(['GET'])
def getInboxReadCount(request, user_name):
    user = Profile.objects.get(name=user_name)
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
        follower = Profile.objects.get(Q(id=follow.user.id))
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


@api_view(['GET'])
def getUserTypeById(request, user_type_id):
    type = Type.objects.get(id=user_type_id)
    serializer = TypeSerializer(type, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    note = Note()
    note.user = Profile.objects.get(id=request.data['user_id'])
    note.title = request.data['title']
    note.content = request.data['content']
    note.note_time = datetime.timedelta(days=30)
    note.save()
    return Response(note.id)
