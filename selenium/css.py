'''css selector css选择器选择元素的方法
1.根据tag名
p {color:red;}               # p后面必须空一格
2.根据ID
#food {color:red;}
3.根据class
.vegetable {color:red;}
4.根据tag名和class名组合
span.vegetable {color:red;}
或 div span.vegetable {color:red;}
------------------------总而言之，随便配合，同一级不空格，不同一级要空格-------------------
--------------------------------
<span class="vegetable good">黄瓜</span>
该句柄表示黄瓜有两个class属性，vegetable和good,只有class有这一特性
对应的语法为：print(driver.find_element_by_css_selector('.vegetable.food'))
-----------------------------------
后代选择器（descendant）
<s1> <s2>        表示选择s1里面的所有s2，s1和s2可以是父子关系也可以不是
#choose_car option
footer p
a b c d {color:red;}
------------------------------------
子（child）选择器
<s1>><s2>
#choose_car>option
a>b>c>d
a b c>d>e f       都可以
------------------------------------
组（group）选择器
<s1>,<s2>
button,p  # 既选择button，又选择p
#food>span,p        注意此处，优先级低于>
#food>span,#food>p   区别与上
#food>*   选择id为food的所有子元素
--------------------------------------
兄弟节点
<s1>+<s2>           选择的s1后面紧跟的弟弟s2
#many>div>p.special+p
<s1>~<s2>           选择的s1后面紧跟的所有弟弟

************************属性选择器*******************************
*[style]                    所有具有style属性的元素，style为不为空不care
p[spec='len2']              找到tag为p，属性spec为len2的元素
p[spec='len2 len3']
p[spec*='len2']             包含len2
p[spec^='len2']             以len2开头
p[spec$='len2']             以len2结尾
p[class='special'][name=p1]  且的关系
----------------------------------------------------
具体第几个子元素
p:nth-child(n)
--------------------------------------------------
'''

from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r'D:\selenium\html\第二次课\s1.html')
print(driver.find_element_by_css_selector('p').text)
print(driver.find_elements_by_css_selector('p'))
print(driver.find_element_by_css_selector('div#food').text)
print(driver.find_element_by_css_selector('.vegetable').text)
print(driver.find_element_by_css_selector('span.vegetable').text)
print(driver.find_element_by_css_selector('div .vegetable').text)
print(driver.find_element_by_css_selector('#many .special').text)
print(driver.find_element_by_css_selector('body .cheese span').text)
print('------------------------a---------------------------------')
a = driver.find_elements_by_css_selector('p,button')
for b in a:
    print(b.text)
print('------------------------b---------------------------------')
print(driver.find_element_by_css_selector('button+div').text)
print('------------------------c---------------------------------')
print(driver.find_element_by_css_selector('div+button').text)
print(driver.find_element_by_css_selector('body p:nth-child(15)').text)     # 表示body的第15个子元素，且该元素tag为p
print(driver.find_element_by_css_selector('body #food p:nth-child(3)').text)
driver.quit()

