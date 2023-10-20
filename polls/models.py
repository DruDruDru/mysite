import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import CustomUser


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    short_description = models.TextField(max_length=200, null=True)
    full_description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='question_images/')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    voted_by = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.choice_text
