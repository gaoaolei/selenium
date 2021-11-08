# coding:utf8
from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('松勤')
driver.find_element_by_id('su').click()


time.sleep(1)
ele = driver.find_element_by_id('1')
print(ele)
print(ele.text)

if ele.text.startswith(u'松勤网 - 松勤软件测试_软件测试在线培训'):
    print('pass')
else:
    print('fail')


driver.quit()