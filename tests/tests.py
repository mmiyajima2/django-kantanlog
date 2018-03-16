# -*- coding: utf8 -*-
from django.test import TestCase
from django.test import Client
from logging import getLogger
from django.urls import reverse
from logusername.models import TObject


logger = getLogger(__name__)


class LogusernameTests(TestCase):

    def setUp(self):
        logger.debug('log user name test name')

    def test_basic(self):
        logger.debug('test_basic')
        client = Client()
        response = client.get(reverse('index'))
        logger.debug(response.__dict__)
        logger.debug(response.content)
        tobject = TObject.objects.get(pk=1)
        logger.debug(str(tobject))
        self.assertIsNotNone(response)
