# -*- coding: utf8 -*-
from threading import local
from logging import getLogger


_tl = local()
logger = getLogger(__name__)


class LogusernameMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        logger.debug('LogusernameMiddleware called')

        if hasattr(request, 'user'):
            _tl.username = getattr(request.user, 'username', '')
        response = self.get_response(request)

        if hasattr(_tl, 'username'):
            del _tl.username

        return response


def get_username():
    return getattr(_tl, 'username', '')
