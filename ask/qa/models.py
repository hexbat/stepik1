# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def resent_questions(self):
        return self.order_by('-added_at')

    def popular_questions(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default='x')
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()


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

