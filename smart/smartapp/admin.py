from django.contrib import admin
from .models import member, Comment

# Register your models here.
admin.site.register(member)
admin.site.register(Comment)
