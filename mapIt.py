#! /usr/bin/env python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

# -*- coding: utf8 -*-

import webbrowser, sys, pyperclip, geocoder
from requests import get


if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.get('chrome').open_new('https://www.google.com/maps/place/' + address)