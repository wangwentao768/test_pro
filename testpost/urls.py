from django.conf.urls import url

from .api import *

urlpatterns = [
    url(r'^testpost/', test_post),
]
