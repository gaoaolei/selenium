'''
refresh() 刷新
forward() 前进
back() 后退
当页面中的有浮现式的页面时，可在console中输入setTimeout(function(){debugger;},5000)
maximize_window()   浏览器最大化
@@@@@@@@@@@@@@@@@@@@@@@@@重要一点：定位元素必须页面最大化@@@@@@@@@@@@@@@@@@@@@@@@@@@@
点击按钮时，定位按钮最好定义btn这一级，不要太精确，因为太精确的可能没有可点击属性
'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
import time
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.find_element_by_id('kw').send_keys('松勤')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()
