# -*- coding: utf-8 -*-
""" Tests """

from __future__ import absolute_import, division, unicode_literals

import logging
import os
import sys

import xbmcaddon

logging.basicConfig(level=logging.DEBUG)

# Add logging to urllib
# import http.client
# http.client.HTTPConnection.debuglevel = 1

# Make UTF-8 the default encoding in Python 2
if sys.version_info[0] == 2:
    reload(sys)  # pylint: disable=undefined-variable  # noqa: F821
    sys.setdefaultencoding("utf-8")  # pylint: disable=no-member

# Set credentials based on environment data
# Use the .env file with Pipenv to make this work nicely during development
if os.environ.get('ADDON_USERNAME') and os.environ.get('ADDON_PASSWORD'):
    ADDON = xbmcaddon.Addon()
    ADDON.setSetting('username', os.environ.get('ADDON_USERNAME'))
    ADDON.setSetting('password', os.environ.get('ADDON_PASSWORD'))
