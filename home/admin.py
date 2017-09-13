from django.contrib import admin

from .models import School, Book, User, Order

# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_no', 'principal_name', 'website', 'code', 'status')
    list_filter = ('name', 'status')
    search_fields = ('name', 'company')


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_name', 'bundle', 'particulars', 'total')
    search_fields = ('name', 'class_name')
    list_filter = ('name', 'class_name', 'bundle')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'school_id', 'name_of_parent', 'mobile_no', 'email_id')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'book_id', 'school_id', 'order_time', 'total', 'processed')
    list_filter = ('school_id', 'order_time', 'processed')


admin.site.register(School, SchoolAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
