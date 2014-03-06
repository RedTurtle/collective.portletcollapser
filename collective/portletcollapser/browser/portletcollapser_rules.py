# -*- coding: utf-8 -*-
from collective.portletcollapser.interfaces import IPortletCollapserSettings
from plone.registry.interfaces import IRegistry
from Products.Five.browser import BrowserView
from zope.component import queryUtility


class JavaScript(BrowserView):
    """Get the registry contents as a JavaScript object literal"""

    JS_LITERAL = """(function ($) {
    $(document).ready(function() {
        %s
    });
})(jQuery);
"""

    HANDLER_SKELETON = """
        $('%s').collapsePortlet({'default_state': '%s'});
        $('%s dt').click( function(event) {
            event.preventDefault();
            $(this).collapsePortlet('toggle');
        });
"""

    def __call__(self, *args, **kwargs):
        self.request.response.setHeader("Content-type", "text/javascript")
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IPortletCollapserSettings, check=False)
        js_string = ""
        for selector in settings.selectors:
            js_string += self.HANDLER_SKELETON % (selector.css_selector, selector.default_state, selector.css_selector) + '\n'
        return self.JS_LITERAL % js_string
