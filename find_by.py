'''
web定位元素的方法总共8种,此页讲了6种，还有两种是by_css_selector和by_xpath
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('file://D:\selenium\html\第二次课\s1.html')
time.sleep(0.1)
ids = driver.find_elements_by_id('choose_car')   # id
for id in ids:
    print(id.text)

eles = driver.find_elements_by_name('an')       # name
for ele in eles:
    print(ele.text)

tags = driver.find_elements_by_tag_name('button')   # tag
for tag in tags:
    print(tag.text)

tags1 = driver.find_elements_by_tag_name('a')   # tag
for tag1 in tags1:
    print(tag1.text)

cheeses = driver.find_elements_by_class_name('cheese')      # class
print(cheeses)
for cheese in cheeses:
    print(cheese.text)
    print(cheese.get_attribute('outerHTML'))

# 两种判断元素存不存在的方法（若找不到元素，用elements时返回[],用element时报错）
noexists = driver.find_elements_by_name('bucunzai')
if noexists:
    print(noexists)
else:
    print('bu cun zai')

try:
    noexist = driver.find_element_by_name('bucunzai')
except:
    print('不存在')

links = driver.find_elements_by_link_text('转到百度')   # link_text
for link in links:
    print(link.text)

links1 = driver.find_elements_by_partial_link_text('度')   # partial_link_text
print(links1)
for link1 in links1:
    print(link1.text)
links1[0].click()

driver.quit()
