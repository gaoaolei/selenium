'''隐式等待
driver.implicitly_wait(10)  对元素每半秒钟查找一次，直至找到，若超过10s仍未找到，抛出异常,不需导入time

'''
# from selenium import webdriver
# driver = webdriver.Chrome()   # 创建webdriver实例对象
# driver.implicitly_wait(20)
# driver.get('http://www.baidu.com')   # 打开百度网页
# input_box = driver.find_element_by_id('kw')   # 找到元素实例对象（输入框）
# input_box.send_keys('松勤')     # 元素调用send_keys方法
# search_button = driver.find_element_by_id('su')     # 找到元素实例对象（百度按钮）
# search_button.click()     # 按钮对象调用click方法
# return_result = driver.find_element_by_id('1')
# print(return_result.text)
# driver.quit()

'''显示等待
假如某一步骤非常耗时，我们不可能所有动作都隐式等待长时间，因此需要对一些特殊的动作进行特殊处理，就是显示等待
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# WebDriverWait(driver, 0.1, 0.5).until(EC.title_is('百度一下，你就知道'), '超时了')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kw')), '超时了')
print(driver.find_element_by_id('su').get_attribute('value'))
#  为什么把等待时间设置很短，依旧不会超时
#  还有很多用法，可点击EC查看

