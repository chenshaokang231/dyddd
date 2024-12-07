# from DrissionPage import SessionPage
#
# page = SessionPage()
# page.get('https://gitee.com/explore')
#
# # 获取包含“全部推荐项目”文本的 ul 元素
# ul_ele = page.ele('tag:ul@text():全部推荐项目')
#
# # 获取该 ul 元素下所有 a 元素
# titles = ul_ele.eles('tag:a')
#
# # 遍历列表，打印每个 a 元素的文本
# for i in titles:
#     print(i.text)

# from DrissionPage import Chromium
#
# tab = Chromium().latest_tab
# tab.get('https://www.baidu.com')
# eles = tab('#s-top-left').eles('t:a')  # 获取左上角导航栏内所有<a>元素
# for ele in eles.filter.displayed():  # 筛选出显示的元素列表并逐个打印文本
#     print(ele.text, end=' ')
#
# from DrissionPage import Chromium
#
# tab = Chromium().latest_tab
# tab.get('https://www.baidu.com')
# eles = tab('#s-top-left').eles('t:a')
# print(eles.get.texts())  # 获取所有元素的文本
# print(eles.filter.displayed().get.texts())  # 获取的元素的文本

from DrissionPage import SessionPage

page = SessionPage()
page.get('https://gitee.com/explore')

# 获取推荐目录下所有 a 元素
li_eles = page('tag:ul@text():推荐项目').eles('t:a')

# 遍历列表
for i in li_eles:
    # 获取并打印标签名、文本、href 属性
    print(i.tag, i.text, i.attribute('href'))
