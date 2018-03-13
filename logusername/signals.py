# -*- coding: utf8 -*-
from logging import getLogger
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .middlewares import get_username


logger = getLogger(__name__)


@receiver(pre_save)
def logusername(sender, **kwargs):
    instance = kwargs['instance']
    logger.debug(sender.__module__)
    if sender.__module__ not in settings.LOGUSERNAME_TARGET_MODNAMES:
        return
    if hasattr(instance, 'created_by') and not getattr(instance, 'created_by'):
        setattr(instance, 'created_by', get_username())
    if hasattr(instance, 'updated_by'):
        setattr(instance, 'updated_by', get_username())
