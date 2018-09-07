with open(r'D:\selenium\html\第二次课\bs1.html', encoding='utf8') as f:
    html_doc = f.read()
from bs4 import BeautifulSoup
# 指定html5lib来解析文档
doc = BeautifulSoup(html_doc, 'html5lib')
print(doc)
print('---------------')
print(doc.find('title'))
print(doc.title)
type(doc.title)
print(doc.title.name)
print(doc.title.text)
print(doc.title.string)
print(doc.title.get_text())
print('---------------')
print(doc.find('div'))
print(doc.div)
print('------------1-------------')
print(doc.div.name)
print(doc.div.text)
print(doc.div.string)             # 不适合获取子元素或前后有空格的text
print(doc.div.get_text())
print(doc.div['id'])   # 获取元素的属性
print('-------------2---------------')
print(doc.div.parent)  # 获取元素的父元素
print('-0---------------3-----------')
print(doc.p['style'])       # 获取元素的属性
print(doc.p['class'])
print(doc.p.get('class'))
print(doc.p.attrs)      # 获取元素的所有属性
print(doc.find_all('a'))    # 找到所有tag=a的元素
print(doc.find_all('a')[0])
print(doc.find_all('a')[0]['href'])
print(doc.find_all('a')[0]['id'])
print(doc.find_all('a')[0]['class'])
print(doc.find_all('a')[0].text)
print(doc.find_all('a')[0].get_text())
# 多条件精确范围查找
print(doc.find('a', href="http://example.com/elsie"))
print(doc.find('a', id="link1"))
print(doc.find('div').find('a'))  # 找到元素中的子元素
print('---------------通过属性查找元素----------------')
print(doc.find(href="http://example.com/elsie"))
# print(doc.find(class="story"))    # ??????
print(doc.find(id="d1"))
print('-------******************************************')
print(type(doc.title))
print(doc.div.get('id'))
del doc.div['id']              # 删除属性
print(doc.div.get('id'))
