from django.conf.urls import url

from school.views import login_view
from . import views
urlpatterns = [
    url(r'^$', login_view, name='login'),

]
