#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://www.baidu.com')

# 鼠标悬停
settingLink = driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).move_to_element(settingLink).perform()

# 点击
driver.find_element_by_link_text('搜索设置').click()
time.sleep(3)

# 触发截屏
driver.get_screenshot_as_file('alert_ScreenShot.png')

# 点击触发Alert
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(3)

# 接受Alert
driver.switch_to.alert.accept()
time.sleep(3)

driver.quit()
