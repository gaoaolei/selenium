from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.execute_script("window.open('https://www.wtzw.com')")     # 需借助前端代码开启新的标签页，但是要注意handle还在第一个上
current_window = driver.current_window_handle
print(current_window)
all_Windows = driver.window_handles
print(all_Windows)
# 切到第二个窗口
# driver.switch_to.window(all_Windows[1])
# 数index很不准，所以要具体定位，如下：
for handle in all_Windows:
    driver.switch_to.window(handle)
    if '梧桐' in driver.title:
        break
a = driver.current_window_handle
print(a)
print(driver.current_url)   # 打印当前标签页的url   asdf