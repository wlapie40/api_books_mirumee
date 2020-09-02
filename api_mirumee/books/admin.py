from django.contrib import admin

from .models import (Authors,
                     Books,
                     Rates)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "created_at")


class BooksAdmin(admin.ModelAdmin):
    list_display = ("id", "isbn", "title", "author", "genres", "created_at")


class RatesAdmin(admin.ModelAdmin):
    list_display = ("id", "rate", "text", "pub_date")


admin.site.register(Authors, AuthorAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Rates, RatesAdmin)
