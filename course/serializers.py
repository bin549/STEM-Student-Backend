from rest_framework import serializers
from .models import Entity, Genre, Selection, Collection, Lecture


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = (
            "id",
            "title",
            "description",
            "cover_img",
            "created_time",
            "owner",
            "genre",
            "get_absolute_url",
            "get_image",
            "get_student_url",
            "serial_number",
        )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            "id",
            "name"
        )


class SelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = (
            "id",
            "user",
            "course",
            "select_time"
        )


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = (
            "id",
            "user",
            "course",
            "collect_time"
        )


class LectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = (
            "id",
            "index",
            "title",
            "created_time",
            "format",
            "course"
        )
