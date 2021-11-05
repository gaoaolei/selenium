'''有的网页分为几个子网页(iframe)，即有多个<html></html>
切换到子frame
driver.switch_to.frame('frame_reference')    frame_reference为name或id属性或index（从0开始）
切回到主html
driver.switch_to.default_content()

https://blog.csdn.net/shifengboy/article/details/114406068
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(60)
driver.maximize_window()
time.sleep(2)
driver.get('http://music.163.com')
time.sleep(2)
driver.switch_to.frame('g_iframe')
time.sleep(2)
l = driver.find_element_by_css_selector("body>a[class='m-back']")
m = driver.find_element_by_css_selector("head>title")
time.sleep(1)
print(l.get_attribute('textContent'))
print(m.get_attribute('textContent'))
# driver.switch_to.default_content()    # 切回主文档
# driver.quit()

#  在19句中不能直接打印l.text，因为这个元素有个hidefocus属性，即为隐藏元素，必须用get_attribute('textContent'),
#  head里面的元素也是这样。



