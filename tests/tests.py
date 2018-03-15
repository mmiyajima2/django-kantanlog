# -*- coding: utf8 -*-
from django.test import TestCase
from logging import getLogger


logger = getLogger(__name__)


class LogusernameTests(TestCase):

    def setUp(self):
        logger.debug('log user name test name')
