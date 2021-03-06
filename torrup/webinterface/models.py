# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Profile(User):
    pass
    
class Tracker(models.Model):
    profile = models.ForeignKey(Profile)
    name = models.CharField(max_length = 500)
    url = models.URLField()
    login = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name
    
class Topic(models.Model):
    tracker = models.ForeignKey(Tracker)
    url = models.URLField()
    name = models.CharField(max_length = 500)
    update_time = models.DateTimeField()            # Сколько времени назад была обновлена раздача
    recheck_time = models.DateTimeField()           # Время проверки состояния раздачи

    def __unicode__(self):
        return self.name

