import datetime
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Type, Message, Follow, Note, Photo
from course.models import Entity
from .serializers import UserSerializer, TypeSerializer, MessageSerializer, NoteSerializer, PhotoSerializer


class ProfileAPI(APIView):

    def get(self, request, user_id, format=None):
        profile = Profile.objects.get(id=user_id)
        serializer = UserSerializer(profile, many=False)
        return Response(serializer.data)

    def post(self, request, format=None):
        profile = Profile()
        profile.username = request.data["username"]
        profile.email = request.data["email"]
        profile.password = request.data["password"]
        profile.name = request.data["username"]
        profile.location = None
        profile.short_intro = None
        profile.bio = None
        profile.profile_image = None
        profile.created_time = datetime.timedelta(days=30)
        profile.type = Type.objects.get(Q(name="student"))
        profile.profile_image = None
        profile.save()
        return Response(1)

class FollowAPI(APIView):

    def get(self, request, format=None):
        if request.query_params.__contains__("option"):
            if request.query_params["option"] == "follower":
                follows = Follow.objects.filter(other_user=request.query_params["user_id"])
                followers = []
                for follow in follows:
                    follower = Profile.objects.get(Q(id=follow.user.id))
                    followers.append(
                        {
                            "id": follower.id
                        }
                    )
                return Response(followers)
            elif request.query_params["option"] == "following":
                follows = Follow.objects.filter(user=request.query_params["user_id"])
                followers = []
                for follow in follows:
                    follower = Profile.objects.get(Q(id=follow.other_user.id))
                    followers.append(
                        {
                            "id": follower.id
                        }
                    )
                return Response(followers)
        else:
            try:
                follow = Follow.objects.get(Q(user=request.query_params['user_id']) & Q(other_user=request.query_params['other_user_id']))
                return Response(1)
            except Exception:
                return Response(0)

    def post(self, request, format=None):
        follow = Follow()
        user = Profile.objects.get(Q(id=request.query_params['user_id']))
        other_user = Profile.objects.get(Q(id=request.query_params['other_user_id']))
        follow.user = user
        follow.other_user = other_user
        follow.follow_time = datetime.timedelta(days=30)
        follow.save()
        return Response(1)

    def delete(self, request, format=None):
        follow = Follow.objects.get(Q(user=request.query_params['user_id']) & Q(other_user=request.query_params['other_user_id']))
        follow.delete()
        return Response(1)


class NoteAPI(APIView):

    def get(self, request, format=None):
        if request.query_params.__contains__("user_id"):
            notes = Note.objects.filter(user=request.query_params["user_id"])
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data)
        elif request.query_params.__contains__("note_id"):
            note = Note.objects.get(id=request.query_params["note_id"])
            serializer = NoteSerializer(note, many=False)
            return Response(serializer.data)


    def post(self, request, format=None):
        note = Note()
        note.user = Profile.objects.get(id=request.query_params['user_id'])
        note.title = request.query_params['title']
        note.content = request.query_params['content']
        note.note_time = datetime.timedelta(days=30)
        note.save()
        return Response(note.id)

    def put(self, request, format=None):
        print(request.query_params)
        note = Note.objects.get(Q(id=request.query_params["note_id"]))
        note.title = request.query_params["title"]
        note.content = request.query_params["content"]
        note.save()
        return Response(1)

    def delete(self, request, format=None):
        note = Note.objects.get(Q(id=request.query_params["note_id"]))
        note.delete()
        return Response(1)

class MessageAPI(APIView):

    def post(self, request, format=None):
        message = Message()
        message.sender = Profile.objects.get(id=request.query_params['sender'])
        message.title = request.query_params['title']
        message.content = request.query_params['content']
        message.is_read = False
        message.created_time = datetime.timedelta(days=30)
        user_type = Type.objects.get(name='manager')
        recipients = Profile.objects.filter(user_type=user_type.id)
        for recipient in recipients:
            message.recipient = recipient
            message.save()
        return Response(1)


class PhotoAPI(APIView):

    def get(self, request, format=None):
        if request.query_params.__contains__("is_cover"):
            photo = Photo.objects.get(Q(user=request.query_params["user_id"]) & Q(is_cover=True))
            serializer = PhotoSerializer(photo, many=False)
            return Response(serializer.data)
        else:
            photos = Photo.objects.filter(Q(user=request.query_params["user_id"])).order_by("upload_time")
            serializer = PhotoSerializer(photos, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        medias = request.data["medias"]
        user = Profile.objects.get(Q(id=request.data["user_id"]))
        for media in medias:
            photo = Photo()
            photo.media = media
            photo.user = user
            photo.upload_time = datetime.timedelta(days=30)
            photo.is_cover = False
            photo.save()
        return Response(1)

    def put(self, request, format=None):
        photos = Photo.objects.filter(Q(user=request.query_params["user_id"]))
        for photo in photos:
            photo.is_cover = False
            photo.save()
        photo = Photo.objects.get(Q(id=request.query_params["photo_id"]))
        photo.is_cover = True
        photo.save()
        return Response(1)

    def delete(self, request, format=None):
        photo = Photo.objects.get(Q(id=request.query_params["photo_id"]))
        photo.delete()
        return Response(1)

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




@api_view(['GET'])
def getUserTypeById(request, user_type_id):
    type = Type.objects.get(id=user_type_id)
    serializer = TypeSerializer(type, many=False)
    return Response(serializer.data)
