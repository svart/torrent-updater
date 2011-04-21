# -*- coding: utf-8 -*-
from django.contrib import admin
from torrup.webinterface.models import Profile, Tracker, Topic

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username',)

class TrackerAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tracker, TrackerAdmin)
admin.site.register(Topic, TopicAdmin)
