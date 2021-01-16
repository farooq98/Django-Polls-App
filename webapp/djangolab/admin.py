from django.contrib import admin
from .models import Question, Options

# Register your models here.
admin.site.register(Question)
admin.site.register(Options)