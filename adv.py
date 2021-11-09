from selenium import webdriver

d = webdriver.Chrome()
d.implicitly_wait(5)
d.maximize_window()
d.get('https://ad-xiaoshuo.qimao.com/backend/manage/reader-paging?t=1636014382949')
d.find_element_by_id('username').send_keys('15171001790')
d.find_element_by_id('password').send_keys('4209841413pl')
# 点击登录
d.find_element_by_css_selector('body > div > div.main.clearfix > form > ul > li:nth-child(6) > a').click()
# 点击章内tab
d.find_element_by_css_selector('#app > div > div.wrapper > aside > div > ul > li:nth-child(3) > a').click()
# # 点击wifi
d.find_element_by_css_selector(
    '#app > div > div.wrapper > div > div.ant-spin-nested-loading > div > div > div.form-wrap > div.ff-box > div.qm-form.t-90 > div > form > div:nth-child(9) > div.ant-col.ant-col-24.ant-form-item-control-wrapper > div > span > div > label:nth-child(2) > span:nth-child(2)').click()

# 输入bidding排序
bid_sort = d.find_element_by_css_selector(
    '#app > div > div.wrapper > div > div.ant-spin-nested-loading > div > div > div.table-wrap.mt > div:nth-child(1) > div.qm-mod-th > div > div > div > form > div:nth-child(1) > div.ant-col.ant-form-item-control-wrapper > div > span > input')

# 输入bidding价格
bid_price = d.find_element_by_css_selector(
    '#app > div > div.wrapper > div > div.ant-spin-nested-loading > div > div > div.table-wrap.mt > div:nth-child(1) > div.qm-mod-th > div > div > div > form > div:nth-child(2) > div.ant-col.ant-form-item-control-wrapper > div > span > div > div.ant-input-number-input-wrap > input')

bid_sort.send_keys(22)
bid_price.send_keys(222)

# 找到所有的数据条数  28条
area = d.find_elements_by_css_selector('.ant-table-row.ant-table-row-level-0')
print(len(area))

ele_data = []
for list in area:
    eles = list.find_elements_by_tag_name('td')     # 找到所有列
    print(eles[0])
    # a = eles[0].text                                # 广告类型
#     b = eles[2].find_element_by_tag_name('input')   # adv_code
#     ele_data.append([a,b])
# print(ele_data)
# for i in ele_data:
#     if i[0].startswith('穿山甲'):      # 广告类型
#         i[1].send_keys('123456789')
#





# 击保存
# d.find_element_by_css_selector(
#     '#app > div > div.wrapper > div > div.ant-spin-nested-loading > div > div > div.btn-list.mt > button').click()