#! /usr/bin/env python3

from selenium import webdriver

webdr = webdriver.Chrome()
webdr.get('https://chrome.google.com')

print('设置浏览器宽480、高800显示')
webdr.set_window_size(480, 800)

webdr.quit()

