"""
sentry-comments
~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 Andi Albrecht <albrecht.andi@gmail.com>
:license: BSD, see LICENSE for more details.
"""

try:
    VERSION = __import__('pkg_resources').get_distribution(__name__).version
except Exception, e:
    VERSION = 'unknown'
