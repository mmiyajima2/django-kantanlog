# -*- coding: utf8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


def cbyuby(cls):

    created_by = models.CharField(
        verbose_name=_('created by'),
        null=False,
        blank=False,
        max_length=100,
    )

    updated_by = models.CharField(
        verbose_name=_('updated by'),
        null=False,
        blank=False,
        max_length=100,
    )

    cls.add_to_class('created_by', created_by)
    cls.add_to_class('updated_by', updated_by)

    return cls
