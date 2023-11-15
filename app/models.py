from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Question(models.Model):
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime = models.DateTimeField()
    rating = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Answer(models.Model):
    tag = models.ManyToManyField(Tag)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField()
    rating = models.PositiveIntegerField()
    correct_flag = models.BooleanField()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signup_date = models.DateTimeField()
    nickname = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()