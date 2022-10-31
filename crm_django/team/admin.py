from django.contrib import admin

# Register your models here.
from .models import Team, Plan

admin.site.register(Team)
admin.site.register(Plan)
