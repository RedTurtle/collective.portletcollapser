# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger("collective.portletcollapser")

from zope.i18nmessageid import MessageFactory
messageFactory = MessageFactory('collective.portletcollapser')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
