from django.contrib import admin

# Register your models here.

from .models import *

# admin.site.register(item)
@admin.register(Monitor, CPU, Keyboard, Mouse)
class ViewAdmin(admin.ModelAdmin):
    pass