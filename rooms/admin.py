from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class RoomTypeAdmin(admin.ModelAdmin):

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumnail")

    def get_thumnail(self, obj):
        return mark_safe(f'<img width="100" src="{obj.file.url}"/>')

    get_thumnail.short_description = "Thumbnail"


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "total_rating",
    )

    inlines = (PhotoInline,)

    list_filter = ("city",)

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )
