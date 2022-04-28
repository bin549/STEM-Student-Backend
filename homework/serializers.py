from rest_framework import serializers
from .models import Assignment, Execution, Media, MediaType, Log


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
            "finish_time",
            "is_excellent",
            "content_text",
            "appraise_star",
            "appraise_text",
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


class LogSerializer(serializers.ModelSerializer):

   class Meta:

       model = Log
       fields = (
           "id",
           "execution",
           "log_type",
           "log_time",
       )
