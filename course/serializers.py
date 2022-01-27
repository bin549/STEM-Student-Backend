from rest_framework import serializers
from .models import Entity, Genre, Selection, Collection


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
