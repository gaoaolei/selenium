'''
对输入框的一些操作
1.清除输入框中已有的内容     a.clear()
2.获取元素属性             a.get_attribute('value')
3.对单选框的进行选择          a.click()  这样就选中了a选项
4.对勾选框的操作
判断是否被选中             a.is_selected()       返回为boolean
例子：    flag = a.selected()
         if flag:
                print('a is already selected')
         else:
                b.click()
5.对下拉框（可单选，复选）的操作
提供了select类   from selenium.webdriver.support.ui import Select
删除所有选择     a.dselect_all()
选中选项        a.select_by_visible_text('男')
'''