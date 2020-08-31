from django.contrib import admin
from .models import (Author,
                     Books,
                     Rates)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "created_at")


class BooksAdmin(admin.ModelAdmin):
    list_display = ("id", "isbn", "title", "author", "genres", "created_at")


class RatesAdmin(admin.ModelAdmin):
    list_display = ("book", "rate", "text", "pub_date")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Rates, RatesAdmin)
