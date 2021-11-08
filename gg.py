from selenium import webdriver
from lxml import etree
import time

d = webdriver.Chrome()
d.maximize_window()
d.get('https://ad-xiaoshuo.qimao.com/backend/manage/reader-paging?t=1636014382949')
d.find_element_by_id('username').send_keys('15171001790')
d.find_element_by_id('password').send_keys('4209841413pl')
#点击登录
d.find_element_by_css_selector('body > div > div.main.clearfix > form > ul > li:nth-child(6) > a').click()
time.sleep(5)
# 点击章内tab
d.find_element_by_css_selector(
    '#app > div > div.wrapper > aside > div > ul > li:nth-child(3) > a').click()
# # 点击wifi
time.sleep(5)
d.find_element_by_css_selector('#app > div > div.wrapper > div > div.ant-spin-nested-loading > div > div > div.form-wrap > div.ff-box > div.qm-form.t-90 > div > form > div:nth-child(9) > div.ant-col.ant-col-24.ant-form-item-control-wrapper > div > span > div > label:nth-child(2) > span:nth-child(2)').click()
# time.sleep(5)
# # 输入bidding排序
# d.find_element_by_css_selector('#app > div > div.wrapper > div > div.ant-spin-nested-loading > div > div > div.table-wrap.mt > div:nth-child(1) > div.qm-mod-th > div > div > div > form > div:nth-child(1) > div.ant-col.ant-form-item-control-wrapper > div > span > input').send_keys('11')
# time.sleep(5)
# # 输入bidding价格
# d.find_element_by_css_selector('#app > div > div.wrapper > div > div.ant-spin-nested-loading > div > div > div.table-wrap.mt > div:nth-child(1) > div.qm-mod-th > div > div > div > form > div:nth-child(2) > div.ant-col.ant-form-item-control-wrapper > div > span > div > div.ant-input-number-input-wrap > input').send_keys(10)
# time.sleep(5)
# 点击保存
# d.find_element_by_css_selector('#app > div > div.wrapper > div > div.ant-spin-nested-loading > div > div > div.btn-list.mt > button').click()

# 找到所有的数据条数  28条
area = d.find_elements_by_css_selector('.ant-table-row.ant-table-row-level-0')
# time.sleep(2)      #  前往不能要等待
print(area)
print(type(area))
print(len(area))
for i in area:
    eles = i.find_elements_by_tag_name('td')        # 找到所有列
    if eles[0].text.startswith('穿山甲'):
        print(eles[0].text)
        # 找排序
        time.sleep(1)
        eles[1].find_element_by_tag_name('div')
        # eles[1].find_element_by_tag_name('input')
