from django.contrib import admin
from .models import Leader, Movie, Category, Cast
# Register your models here.


class adminMovieList(admin.ModelAdmin):
    list_display = ("name", "cast", "budget")
admin.site.register(Movie, adminMovieList)
admin.site.register(Cast)
admin.site.register(Category)
admin.site.register(Leader)

# 