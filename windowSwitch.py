#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import logging, time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.douban.com/')

mainPage = driver.current_window_handle
logging.debug('Current window handles: %s' % mainPage)

linkMovie = driver.find_element_by_class_name('lnk-movie')
linkMovie.click()

allHandles = driver.window_handles
logging.debug('Current window handles: %s' % allHandles)

for handle in allHandles:
    if handle != mainPage:
        driver.switch_to.window(handle)
        print('Now change to window: %s' % driver.title)
        navlogin = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text('登录/注册'))
        navlogin.click()
        loginTab = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name('account-tab-account'))
        loginTab.click()
        driver.find_element_by_css_selector('#username').send_keys('12345678900')
        driver.find_element_by_css_selector('#password').send_keys('123456', Keys.ENTER)
        # TODO: Check result of login

time.sleep(5)
driver.quit()
print('Done.')
