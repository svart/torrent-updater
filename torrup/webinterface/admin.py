# -*- coding: utf-8 -*-
from django.contrib import admin
from webinterface.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tracker)
admin.site.register(Topic)
