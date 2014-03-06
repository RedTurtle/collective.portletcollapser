# -*- coding: utf-8 -*-
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import quickInstallProduct
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing import z2
from zope.configuration import xmlconfig


class PortletCollapserLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.portletcollapser
        xmlconfig.file('configure.zcml',
                       collective.portletcollapser,
                       context=configurationContext)
        z2.installProduct(app, 'collective.portletcollapser')

    def setUpPloneSite(self, portal):
        quickInstallProduct(portal, 'collective.portletcollapser')
        setRoles(portal, TEST_USER_ID, ['Member', 'Manager'])


PORTLET_COLLAPSER_FIXTURE = PortletCollapserLayer()
PORTLET_COLLAPSER_INTEGRATION_TESTING = IntegrationTesting(bases=(PORTLET_COLLAPSER_FIXTURE, ),
                                                            name="PortletCollapser:Integration")

