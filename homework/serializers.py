from rest_framework import serializers
from .models import Assignment


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
