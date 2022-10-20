from django.contrib import admin
from .models import investigations, bugs, tips
# Register your models here.

admin.site.register(investigations)
admin.site.register(bugs)
admin.site.register(tips)