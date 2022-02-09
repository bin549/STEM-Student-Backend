from rest_framework import serializers
from .models import Profile, Type


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
        model = Profile
        fields = (
            "id",
            "name",
        )
