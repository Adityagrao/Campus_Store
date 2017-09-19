from django.conf.urls import url
from django.contrib import admin
from . import views

admin.site.site_header = "Campus Store Super Admin"
admin.site.site_title = "Campus Store Super Admin"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^parent-login/$', views.parent_login),
    url(r'^parent-register/$', views.parent_register)

]
