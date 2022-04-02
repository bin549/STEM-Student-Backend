from rest_framework import serializers
from .models import Assignment, Execution, Media, MediaType


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:

        model = Assignment
        fields = (
            "id",
            "intro",
            "description",
            "start_time",
            "end_time",
            "course",
        )


class ExecutionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Execution
        fields = (
            "id",
            "score",
            "finish_time",
            "is_excellent",
            "content_text",
            "homework",
            "user",
        )


class MediaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Media
        fields = (
            "id",
            "media",
            "execution",
            "type",
            "get_media",
        )


class MediaTypeSerializer(serializers.ModelSerializer):

   class Meta:

       model = MediaType
       fields = (
           "id",
           "name",
       )
