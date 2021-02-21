'''获取元素属性get_attribute('属性名称')
get_attribute('href')
get_attribute('style')
get_attribute('innerHTML')
get_attribute('outerHTML')
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('file://D:\selenium\html\第二次课\s1.html')
time.sleep(0.1)
# 获取元素属性
ele1 = driver.find_element_by_id('baidulink')
print(ele1.get_attribute('href'))

ele2 = driver.find_element_by_id('food')
print(ele2.get_attribute('style'))
print(ele2.get_attribute('outerHTML'))
print(ele2.get_attribute('innerHTML'))
