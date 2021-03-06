============
Kantan Log
============

.. image:: https://travis-ci.org/mmiyajima2/django-kantanlog.svg?branch=master
    :target: https://travis-ci.org/mmiyajima2/django-kantanlog


.. image:: https://coveralls.io/repos/github/mmiyajima2/django-kantanlog/badge.svg?branch=master
	:target: https://coveralls.io/github/mmiyajima2/django-kantanlog?branch=master


Kantan log is a simple Django helper app.
This app supports logging to Django Model's created_by, updated_by. At http requests interception, too.


Installation
===============

.. code:: bash

  shell>pip install djangokantanlog

Usage
===============
Installed apps:

.. code:: python

  INSTALLED_APPS = [
    ...
    'kantanlog.apps.KantanlogConfig',
  ]
  
Middleware:

.. code:: python

  MIDDLEWARE = [
    ...
    'kantanlog.middlewares.KantanlogMiddleware',
  ]


Settings
===============

KLOG_TARGET_APP_LABELS
-------------------------

Default: ``()``

Target apps, settings as app-label:

.. code:: python

  KLOG_TARGET_APP_LABELS = (
    ...
    'myapp',
  )
  
KLOG_BACKEND
---------------

Default: ``kantanlog.backends.KantanlogDefaultBackend``

As interface, getting user.

e.g.

.. code:: python

  # at settings.py
  KLOG_BACKEND = 'dotted.path.to.MyappBackend'

  ...

  # -*- coding: utf8 -*-
  from logging import getLogger
  from kantanlog.backends import KantanlogDefaultBackend
  from rest_framework_jwt.authentication import JSONWebTokenAuthentication
  from rest_framework_jwt.settings import api_settings


  logger = getLogger(__name__)
  payload_handler = api_settings.JWT_PAYLOAD_HANDLER
  encode_handler = api_settings.JWT_ENCODE_HANDLER


  class MyappBackend(KantanlogDefaultBackend):

      def __init__(self):
          super().__init__()

      def get_user(self, request):
          user = super().get_user(request)
          if user.is_authenticated:
              return user
          ja = JSONWebTokenAuthentication()
          if ja.get_jwt_value(request):
              user, jwt = ja.authenticate(request)
              return user
          return user 
