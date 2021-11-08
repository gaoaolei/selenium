# coding:utf8
from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()

ele = driver.find_element_by_id('su')
print(ele.tag_name)
print(ele.text)
print(ele.size)
print(ele.parent)
print(ele.id)
print(ele.get_attribute(type))






