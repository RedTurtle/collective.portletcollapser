# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from plone.app.registry.browser import controlpanel
from z3c.form import button
from collective.portletcollapser.interfaces import IPortletCollapserSettings
from collective.portletcollapser import messageFactory as _


class PortletCollapserEditForm(controlpanel.RegistryEditForm):
    """collective.navigationtoggle settings form.
    """
    schema = IPortletCollapserSettings
    id = "PortletCollapserSettingsEditForm"
    label = _(u"Portlet Collapser Settings")
    description = _(u"help_portletcollapser_settings_editform",
                    default=u"Manage on which elements the portlet collapser plugin must be activated")

    @button.buttonAndHandler(_('Save'), name='save')
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        changes = self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(_(u"Changes saved"),
                                                      "info")
        self.context.REQUEST.RESPONSE.redirect("@@portletcollapser-settings")

    @button.buttonAndHandler(_('Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(_(u"Edit cancelled"),
                                                      "info")
        self.request.response.redirect("%s/%s" % (self.context.absolute_url(),
                                                  self.control_panel_view))

    @button.buttonAndHandler(_('Save and invalidate JS cache'), name='save_and_invalidate')
    def handleSaveAndInvalidate(self, action):
        PortletCollapserEditForm.handleSave(self, action)
        portal_js = getToolByName(self.context, 'portal_javascripts')
        portal_js.cookResources()
        IStatusMessage(self.request).addStatusMessage(_(u"JavaScript registry invalidated"),
                                                      "info")

    def updateWidgets(self):
        super(PortletCollapserEditForm, self).updateWidgets()
        self.widgets['selectors'].klass += u' selectorSettings'


class PortletCollapserSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Portlet collapser settings control panel.
    """
    form = PortletCollapserEditForm
