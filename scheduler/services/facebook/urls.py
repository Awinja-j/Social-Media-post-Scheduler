from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .facebook_login import FacebookLoginFlow, FacebookCallback

urlpatterns = [
    path('login', FacebookLoginFlow.as_view()),
    path('callback',FacebookCallback.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)