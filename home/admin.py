from django.contrib import admin
from .models import Film,Time,Seat

# Register your models here.


class FilmAdmin(admin.ModelAdmin):
    list_display = ("name","img")

class TimeAdmin(admin.ModelAdmin):
    list_display = ("pro","time")

class SeatAdmin(admin.ModelAdmin):
    list_display = ("sro","total","available")



admin.site.register(Film , FilmAdmin)
admin.site.register(Time , TimeAdmin)
admin.site.register(Seat , SeatAdmin)