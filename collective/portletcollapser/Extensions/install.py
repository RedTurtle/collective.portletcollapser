# -*- coding: utf-8 -*-
from collective.portletcollapser import logger


def uninstall(portal, reinstall=False):
    if not reinstall:
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile('profile-collective.portletcollapser:uninstall')
        logger.info("Uninstall complete")
