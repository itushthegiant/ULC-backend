from django.contrib import admin

from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.Property)
admin.site.register(models.Unit)