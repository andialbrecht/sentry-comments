.. sentry-comments documentation master file, created by
   sphinx-quickstart on Sun Nov 25 10:43:59 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to sentry-comments's documentation!
===========================================

sentry-comments is an extension for Sentry to add comments to events.

**Important Notice** Sentry (>=6.4) supports adding notes to events out-of-the-
box. So there's no need for this extension anymore.


Comments show up as a new action on the event page:

.. image:: img/event.png
   :width: 90%

The comments panel:

.. image:: img/comments.png
   :width: 90%


Installation
------------

To install the comments extension run::

  pip install sentry-comments

Then add ``sentry_comments`` to the ``INSTALLED_APPS`` list in your Sentry
configuration::

    INSTALLED_APPS += ('sentry_comments',)

Run :command:`sentry --config=your.conf.py upgrade` to create the new tables
required by this plugin.

After restarting Sentry you need to enable the plugin for each project on the
project's setting page. A new comments panel appears on the event page. Click
on the panel title to read or add comments.


Configuration
-------------

There are no configuration options yet.


Resources
---------

Bug tracker
  https://github.com/andialbrecht/sentry-comments/issues

Source code
  https://github.com/andialbrecht/sentry-comments

Documentation
  https://sentry-comments.readthedocs.org/


License
-------

sentry-comments is licensed under the BSD license.

.. include:: ../LICENSE

.. Contents:

.. .. toctree::
..    :maxdepth: 2



.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

