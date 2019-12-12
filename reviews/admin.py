from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ review admin """

    list_display = ("room", "user", "get_average")

