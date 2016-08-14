from django.conf.urls import url, include
from nms.views import main

urlpatterns = [
    url(r'^main$', main.home),
]