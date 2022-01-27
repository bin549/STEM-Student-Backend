import uuid
from django.db import models
from users.models import Profile


class Genre(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s' % self.name


class Entity(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cover_img = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title


class Selection(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Entity, null=True, blank=True, on_delete=models.CASCADE)
    select_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.id


class Collection(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Entity, null=True, blank=True, on_delete=models.CASCADE)
    collect_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.id


class Format(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name


class Lecture(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    index = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    format = models.ForeignKey(Format, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Entity, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title
