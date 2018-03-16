from django.views.generic.base import View
from django.http import HttpResponse
from .models import TObject
from logging import getLogger


logger = getLogger(__name__)


class IndexView(View):

    http_method_names = [
        'get',
    ]

    def get(self, request, *args, **kwargs):
        logger.info('tests index...')
        tobject = TObject(name='XYZ')
        res = tobject.save()
        return HttpResponse(
            '{"res": "%s"}' % str(res),
            content_type='application/json'
        )
