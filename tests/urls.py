# -*- coding: utf8 -*-
from django.contrib import admin
from django.urls import path
from .views import IndexView


urlpatterns = [
    path('index/', IndexView.as_view(), name="index"),
    path('admin/', admin.site.urls),
]
