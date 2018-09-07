from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
mainWindow = driver.current_window_handle
driver.find_element_by_css_selector('#jgwab').click()

print(mainWindow)
time.sleep(1)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if '全国' in driver.title:
        break
driver.switch_to.window(mainWindow)
