from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, register
from .models import Worker


@register(Worker)
class WorkerAdmin(ModelAdmin):
    pass
