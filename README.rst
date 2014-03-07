A Plone plugin that add **expand/collapse** functionality to portlets.

.. contents:: **Table of contents**

Introduction
============

Scope of this product is to make possible to add expand/collapse behaviour to Plone portlets programmatically without any modification to the portlet templates, or any needs to override its features.

This product is just a Javascript add-on that rely on native Plone's
`jQuery`__ support.

__ http://jquery.com/

When you will like this?
------------------------

collective.portletcollapser is useful when you have a lot of portlets in side columns.
In this case the columns could be very long, and the users can loose some informations.

If we collapse some secondary portlets, we can gain some space and keep these informations available for the users. They only need to expand them.

This plugin store portlets status in `browser's sessionStorage <https://developer.mozilla.org/en-US/docs/Web/Guide/API/DOM/Storage>`_. This means that if the user expand/collapse certain portlets, the plugin save the status for current browser session. Opening a new tab generates a new session.

Detailed documentation
======================

Basic configuration
-------------------

In your Plone configuration panel you'll find the new "*Portlet collapser settings*".

.. image:: http://blog.redturtle.it/pypi-images/collective.portletcollapser/collective.portletcollapser-controlpanel/image_preview
   :alt: Setup of Portlet collapser configuration
   :target: http://blog.redturtle.it/pypi-images/collective.portletcollapser/collective.portletcollapser-controlpanel

From this controlpanel you can enable a list of portlets with expand/collapse setting two fields:

* CSS selector: the CSS marker for a certain portlet. It could be a class or an id. For example **.portletNavigationTree**
* Portlet default state: could be *expanded* or *collapsed*

Versions/Dependencies
=====================

Plone
-----

* Plone 3.3 (classic Plone theme)
* Plone 4.2 (classic Plone theme and Sunburst)
* Plone 4.3 (classic Plone theme and Sunburst)

Dependencies
------------

* jQuery 1.3 or better
* `plone.app.registry`__

__ http://pypi.python.org/pypi/plone.app.registry

Cache controls
==============

Toggle configuration are stored in a JavaScript file that your browser and Plone *portal_javascript* tool
will probably cache.

When changing configuration you can use the "*Save and invalidate JS cache*" button.

Credits
=======

Developed with the support of:

* `Azienda USL Ferrara`__

  .. image:: http://www.ausl.fe.it/logo_ausl.gif
     :alt: Azienda USL logo

All of them supports the `PloneGov initiative`__.

__ http://www.ausl.fe.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
