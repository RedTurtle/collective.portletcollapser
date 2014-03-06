# -*- coding: utf-8 -*-
from Acquisition import aq_get
from collective.portletcollapser import messageFactory as _
from plone.registry.field import PersistentField
from z3c.form.object import registerFactoryAdapter
from zope import schema
from zope.i18n import translate
from zope.interface import Interface, implements
from zope.schema.vocabulary import SimpleVocabulary

try:
    from zope.app.schema.vocabulary import IVocabularyFactory
except ImportError:
    from zope.schema.interfaces import IVocabularyFactory


class PortletStateVocabulary(object):
    """Vocabulary factory for CPI Emails
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        context = getattr(context, 'context', context)
        request = aq_get(context, 'REQUEST', None)

        return SimpleVocabulary.fromItems((
                      (translate(_(u"Collapsed"), context=request), "collapsed"),
                      (translate(_(u"Expanded"), context=request), "expanded"),))


PortletStateVocabularyFactory = PortletStateVocabulary()


class ICollapserSettingsField(Interface):
    css_selector = schema.ASCIILine(title=_("collapser_cssselector_title", default=u"Portlet CSS Selector"),
                                 description=_("collapser_cssselector_help",
                                               default=u"Insert a css selector for the portlet where you want to activate the expand/collapse behaviour. For example 'dl.myPortletClass'."),
                                 required=True)
    default_state = schema.Choice(title=_("collapser_defaultstate_title", default=u"Portlet default state"),
                                  description=_("collapser_defaultstate_help",
                                               default=u"Select default state for this portlet."),
                                  required=False,
                                  vocabulary="portletcollapser-portlestates-vocabulary")


class CollapserSettingsField(object):
    implements(ICollapserSettingsField)


class PersistentObject(PersistentField, schema.Object):
    pass

registerFactoryAdapter(ICollapserSettingsField, CollapserSettingsField)
