#! /usr/bin/env python3

from selenium import webdriver

webdr = webdriver.Chrome()
webdr.get('https://chrome.google.com/webstore/category/extensions')

print(webdr.find_element_by_id('searchbox-input'))
print(webdr.find_element_by_css_selector("#searchbox-input"))
print(webdr.find_element_by_id('searchbox-input') == webdr.find_element_by_css_selector("#searchbox-input"))
print(webdr.find_elements_by_class_name('FokDXb.g-Qc-s')) # ' ' in class name -> '.'
print(webdr.find_elements_by_class_name('SUBrWc'))
print(webdr.find_element_by_css_selector('.SUBrWc'))
print(webdr.find_elements_by_class_name('SUBrWc') == webdr.find_element_by_css_selector('.SUBrWc'))
print(webdr.find_elements_by_link_text('隐私权政策'))

webdr.quit()

