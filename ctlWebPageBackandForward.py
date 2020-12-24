#! /usr/bin/env python3

from selenium import webdriver
import time

webdr = webdriver.Chrome()
firstUrl = 'https://www.google.com/'
print('Access to %s' % firstUrl)
webdr.get(firstUrl)

time.sleep(3)
secondUrl = 'https://chrome.google.com/webstore/category/extensions'
print('Access to %s' % secondUrl)
webdr.get(secondUrl)

time.sleep(3)
print('Back to %s' % firstUrl)
webdr.back()

time.sleep(3)
print('Forward to %s' % secondUrl)
webdr.forward()

time.sleep(3)
print('Refresh %s' % secondUrl)
webdr.refresh()

time.sleep(3)
webdr.quit()

