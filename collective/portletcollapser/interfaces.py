# -*- coding: utf-8 -*-
from collective.portletcollapser import messageFactory as _
from collective.portletcollapser.custom_fields import ICollapserSettingsField, PersistentObject
from zope import schema
from zope.interface import Interface


class IPortletCollapserLayer(Interface):
    """Layer interface for collective.portletcollapser"""


class IPortletCollapserSettings(Interface):
    """collective.navigationtoggle settings"""

    selectors = schema.Tuple(
          title=_(u'Portlets configuration'),
          description=_('help_selectors',
                        default=u"Insert a list portlets configurations."),
          value_type=PersistentObject(ICollapserSettingsField,
                          title=_(u"Portlet"),
                          description=_("selectors_portlet_help",
                            default=u"For each portlet, insert a CSS selector and default state.")
                          ),
          required=False,
          default=(),
          missing_value=())
