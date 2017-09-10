from django.conf.urls import url

from school.views import login_view, parent_user, school_admin, super_admin
from . import views
urlpatterns = [
    url(r'^$', login_view, name='login'),
    url(r'^parent/', parent_user),
    url(r'^school_admin/', school_admin),
    url(r'^super_admin/', super_admin)
]
