from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404


def user_avatar_upload_path(instance, filename):
    return f"images/profile_pics/{filename}"

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(
        null=True,
        upload_to=user_avatar_upload_path,
        default="images/avatar.svg"
    )

    def save(self, *args, **kwargs):
        if self.id:
            existing = get_object_or_404(User, id=self.id)
            if existing.avatar != self.avatar:
                existing.avatar.delete(save=False)
        super(User, self).save(*args, **kwargs)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


# class Member(models.Model):


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #  a room only have one topic, a topic can have many rooms
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
