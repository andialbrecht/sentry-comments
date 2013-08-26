sentry-comments
===============

sentry-comments is an extension for Sentry which lets you add comments
to sentry events.

.. image:: https://sentry-comments.readthedocs.org/en/latest/_images/event.png
   :width: 90%


Installation
============

To install the comments extension run::

  pip install sentry-comments

Then add ``sentry_comments`` to the ``INSTALLED_APPS`` list in your Sentry
configuration::

    INSTALLED_APPS += ('sentry_comments',)

Run ``sentry --config=your.conf.py upgrade`` to create the new tables
required by this plugin.


License
=======

sentry-comments is licensed under the BSD license.
