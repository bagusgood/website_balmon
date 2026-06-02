from django.contrib import admin

# Register your models here.
from . import models

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'publish', 'update']

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Banner)