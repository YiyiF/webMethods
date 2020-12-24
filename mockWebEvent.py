#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

print('Mock begin...')
webdr = webdriver.Chrome()
webdr.get('https://chrome.google.com/webstore/category/extensions')
print('Driver webdr: %s' % webdr)
searchBox = webdr.find_element_by_id('searchbox-input')
size = searchBox.size
print('The search box info: %s \n            size: %s' % (searchBox, size))

clearBtn = webdr.find_element_by_class_name('n-j-Qc-tg') # clear searchbox btn
print('No input, show clear btn: %s ' % clearBtn.is_displayed())
time.sleep(3)
# Mock input
searchBox.send_keys('crxMouse')
# Mock enter
# time.sleep(3)
# searchBox.submit()

time.sleep(3)
print('Input, then show clear btn: %s ' % clearBtn.is_displayed())
clearBtn.click() # Click clear btn
print('Clicked, show clear btn: %s ' % clearBtn.is_displayed())


# Mock click a link -- The first recommend extension
firstExtensionLink = webdr.find_elements_by_css_selector('.a-P-d-w')

time.sleep(3)
print('To click first extension: %s' % firstExtensionLink[0].get_attribute('title'))
firstExtensionLink[0].click()
elemText = firstExtensionLink[0].text
print('To click first extension: %s' % elemText)

time.sleep(3)
breadcrumbBtn = WebDriverWait(webdr, 10).until(lambda webdr: webdr.find_elements_by_link_text('扩展程序')) # 在10s内智能等待查找元素加载完成

# breadcrumbBtn = webdr.find_elements_by_link_text('扩展程序')
print('Breadcrumb button: %s' % breadcrumbBtn)
breadcrumbBtn[0].click()
time.sleep(5)
webdr.quit()
print('Mock done.')
