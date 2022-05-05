from rest_framework import serializers
from .models import Profile, Type, Message, Note, Photo


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = Profile
        fields = (
            "id",
            "name",
            "email",
            "username",
            "location",
            "short_intro",
            "bio",
            "profile_image",
            "created_time",
            "user_type",
            "get_image",
        )


class TypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Type
        fields = (
            "id",
            "name",
        )


class MessageSerializer(serializers.ModelSerializer):

    class Meta:

        model = Message
        fields = (
            "id",
            "sender",
            "recipient",
            "title",
            "content",
            "is_read",
            "created_time",
        )


class NoteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Note
        fields = (
            "id",
            "user",
            "title",
            "content",
            "note_time",
        )

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Photo
        fields = (
            "id",
            "media",
            "upload_time",
            "is_cover",
            "user",
        )
