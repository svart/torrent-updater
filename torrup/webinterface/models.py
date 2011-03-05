# -*- coding: utf-8 -*-
from django.db import models

class Profile(models.Model):
    login = models.CharField(max_length = 100)
    pass_hash = models.CharField(max_length = 550)
    
class Tracker(models.Model):
    profile = models.ForeignKey(Profile)
    name = models.CharField(max_length = 500)
    url = models.URLField()
    login = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    
class Topic(models.Model):
    tracker = models.ForeignKey(Tracker)
    url = models.URLField()
    name = models.CharField(max_length = 500)
    update_time = models.DateTimeField()            # Сколько времени назад была обновлена раздача
    recheck_time = models.DateTimeField()           # Время проверки состояния раздачи

