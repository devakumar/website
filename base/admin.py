from django.contrib import admin

# Register your models here.
from .models import Event

#class EventAdmin(admin.ModelAdmin):

admin.site.register(Event)