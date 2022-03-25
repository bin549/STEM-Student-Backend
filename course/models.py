from django.db import models
from users.models import Profile
import uuid
import os


class Genre(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s' % self.name


class Entity(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    cover_img = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=False, null=True)
    serial_number = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return f'/course/{self.title}/'

    def get_image(self):
        if self.cover_img:
            return self.cover_img.url
        return ''

    def get_student_url(self):
        return f'/course_student/{self.id}/'


class Selection(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Entity, null=True, blank=True, on_delete=models.CASCADE)
    select_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.id


class Wishlist(models.Model):

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
    media = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/about-us-video.mp4")
    format = models.ForeignKey(Format, null=True, blank=True, on_delete=models.CASCADE)
    is_preview = models.BooleanField(default=False, null=True)
    course = models.ForeignKey(Entity, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return f'/course/{self.course.title}/learn/{self.id}/'

    def get_media(self):
        if self.media:
            return self.media.url
        return ''


class Comment(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, null=True, blank=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        ordering = ['comment_time']
