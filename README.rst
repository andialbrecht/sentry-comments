sentry-comments
===============

.. image:: https://travis-ci.org/andialbrecht/sentry-comments.png?branch=master
   :target: https://travis-ci.org/andialbrecht/sentry-comments

sentry-comments is an extension for Sentry which lets you add comments
to sentry events.

**Important Notice** Sentry (>=6.4) supports adding notes to events out-of-the-
box. So there's no need for this extension anymore.

.. image:: https://sentry-comments.readthedocs.org/en/latest/_images/event.png
   :width: 90%


Installation
============

To install the comments extension run::

  pip install sentry-comments

Then add ``sentry_comments`` to the ``INSTALLED_APPS`` list in your Sentry
configuration::

    INSTALLED_APPS += ('sentry_comments',)

(See https://github.com/getsentry/sentry/issues/1042 why this is needed.)

Run ``sentry --config=your.conf.py upgrade`` to create the new tables
required by this plugin.


Demo
====

To run a demo instance with this plugin locally::

  cd demo/
  ./mkdemo.sh

You'll need ``virtualenv`` in your PATH to run this script.


License
=======

sentry-comments is licensed under the BSD license.
