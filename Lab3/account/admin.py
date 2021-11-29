from django.contrib import admin
from .models import Profile
from django.urls import path

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
