# -*- coding: utf8 -*-
from django.apps import AppConfig


class LogusernameConfig(AppConfig):

    name = 'logusername'

    def ready(self):
        from . import signals # noqa
