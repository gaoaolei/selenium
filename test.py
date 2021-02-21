from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://www.baidu.com')
print(driver.current_url)               # 打印网址
print(driver.name)                      # 打印浏览器名字
print(driver.title)                     # 打印网址标题
# driver.find_element_by_css_selector('#u1>a[name="tj_login"]').click()
print(driver.find_element_by_css_selector('#u1>a[name="tj_login"]').size)
print(driver.find_element_by_css_selector('#u1>a[name="tj_login"]').is_displayed())
print(driver.find_element_by_css_selector('#u1>a[name="tj_login"]').is_enabled())
print(driver.find_element_by_css_selector('#u1>a[name="tj_login"]').is_selected())
# driver.delete_all_cookies()
# driver.delete_cookie("cookiename")
print(driver.find_element_by_css_selector('#u1>a[name="tj_login"]').value_of_css_property('#u1>a[name'
                                                                                          '="tj_login"]'))
# time.sleep(3)
# driver.find_element_by_css_selector('div>.tang-pass-footerBarULogin').click()
# time.sleep(3)
# driver.find_element_by_css_selector('#TANGRAM__PSP_10__userName').send_keys('GAL586483')
# time.sleep(3)
# driver.find_element_by_css_selector('#TANGRAM__PSP_10__password').send_keys('4209841413pl')
# time.sleep(3)
# driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
# # driver.find_element_by_id('TANGRAM__PSP_10__form').submit()