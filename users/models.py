import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Type(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    created_time = models.DateTimeField(auto_now_add=True)
    user_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.username)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

    def get_image(self):
        if self.profile_image:
            return self.profile_image.url
        return ''


class Message(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.id


class Follow(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, unique=False, null=True, blank=True)
    other_user = models.OneToOneField(Profile, on_delete=models.CASCADE,  unique=False, null=True, blank=True, related_name="other_user")
    follow_time = models.DateTimeField(auto_now_add=True)


class Note(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    note_time = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    media = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    upload_time = models.DateTimeField(auto_now_add=True)
    is_cover = models.BooleanField(default=False, null=True)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, unique=False, null=True, blank=True)

    def get_image(self):
        if self.media:
            return self.media.url
        return ''
