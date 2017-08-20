from django.contrib import admin

# Register your models here.
from .models import School, Book


class SchoolAdmin(admin.ModelAdmin):
    pass


admin.site.register(School, SchoolAdmin)


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
