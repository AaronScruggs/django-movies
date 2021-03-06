from django.contrib import admin
from moviestuff.models import Movie, Link, Genre, Rating, Tag


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "genres", "created_at", "modified_at")


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "imdbid", "tmdbid", "created_at", "modified_at")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("genres", "created_at", "modified_at")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("userid", "rating", "created_at", "modified_at")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("userid", "tag", "created_at", "modified_at")
