# -*- coding: utf-8 -*-
import unittest
from zope import interface
from zope.component import getMultiAdapter, queryUtility
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import logout
from plone.registry.interfaces import IRegistry
from collective.portletcollapser.interfaces import IPortletCollapserLayer
from collective.portletcollapser.interfaces import IPortletCollapserSettings
from collective.portletcollapser.testing import PORTLET_COLLAPSER_INTEGRATION_TESTING
from collective.portletcollapser.custom_fields import CollapserSettingsField


class TestConfigurationJSView(unittest.TestCase):

    layer = PORTLET_COLLAPSER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        # to be removed when p.a.testing will fix https://dev.plone.org/ticket/11673
        interface.alsoProvides(self.request, IPortletCollapserLayer)
        registry = queryUtility(IRegistry)
        self.settings = registry.forInterface(IPortletCollapserSettings, check=False)
        self.js_view = getMultiAdapter((self.portal, self.request), name=u"collective.portletcollapser.rules.js")

    def test_portletcollapser_controlpanel_view(self):
        """
        test if there is settings view
        """
        view = getMultiAdapter((self.portal, self.request), name="portletcollapser-settings")
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_portletcollapser_controlpanel_view_protected(self):
        """
        test if the settings view is protected
        """
        from AccessControl import Unauthorized
        logout()
        self.assertRaises(Unauthorized, self.portal.restrictedTraverse, '@@portletcollapser-settings')

    def test_custom_jsview(self):
        new_setting = CollapserSettingsField()
        new_setting.css_selector = ".portletNavigationTree"
        new_setting.default_state = "collapsed"
        self.settings.selectors = (new_setting, )
        str_result = """
        $('.portletNavigationTree').collapsePortlet({'default_state': 'collapsed'});
        $('.portletNavigationTree dt').click( function(event) {
            event.preventDefault();
            $(this).collapsePortlet('toggle');
        });
"""
        self.assertTrue(str_result in self.js_view())
