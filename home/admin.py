from django.contrib import admin

# Register your models here.
from .models import School, Book


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_no', 'principal_name', 'website', 'code', 'status')
    list_filter = ('name', 'status')
    search_fields = ('name', 'company')


class BookAdmin(admin.ModelAdmin):
    list_display = ('School_name', 'class_name', 'bundle', 'particulars', 'total')
    search_fields = ('School_name', 'class_name')
    list_filter = ('School_name','class_name','bundle')


admin.site.register(School, SchoolAdmin)
admin.site.register(Book, BookAdmin)
