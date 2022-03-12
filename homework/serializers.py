from rest_framework import serializers
from .models import Assignment, Execution


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
            "content_media",
            "homework",
            "user",
            "get_media"
        )
