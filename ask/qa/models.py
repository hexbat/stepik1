# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default='x')
    likes = models.ManyToManyField(User, related_name='question_like_user')


class QuestionMnager(models.Manager):
    def new(self):
        return Question.objects.order_by('added_at').desc()

    def popular(self):
        return Question.objects.order_by('rating').desc()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, default='x')


class Likes(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="like_question"
    )
    user = models.ForeignKey(
        User,
        related_name="like_user"
    )
