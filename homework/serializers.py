from rest_framework import serializers
from .models import Assignment, Execution


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = (
            "id",
            "intro",
            "start_time",
            "end_time",
            "course",
        )


class ExecutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = (
            "id",
            "score",
            "is_finish",
            "is_excellent",
            "homework",
            "user"
        )
