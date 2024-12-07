# from DrissionPage import Chromium,SessionPage
# import ddddocr
# from loguru import logger
# from DataRecorder import Recorder
# from threading import Thread
# 1.模式选择
# 浏览器模式，
# 封装的requests库中的session、cookie；
# 2.元素查找
# 3.行为链
# 监听listen、执行js代码
# 4.downloadkit 下载，异步多线程
# 5.recorder记录和保存

# browser = Chromium()
# tab = browser.latest_tab
# tab.get('https://www.baidu.com')
# ele = tab.ele('#kw')
#
# r.add_data('test')
# r.record()

import asyncio
from DrissionPage import Chromium
from DataRecorder import Recorder
# 多线程主要用threading和concurrent.futures
# threading 模块用于基于线程的并发，
# asyncio 模块用于基于协程的并发。
# 这个是操作浏览器，换另外一种，用监听接口的方式接收数据
# recorder.add_data
#
# async def collect_data(tab, recorder, title, num=1):
#     # 遍历所有标题元素并记录到记录器
#     for i in tab.eles('.title project-namespace-path'):
#         recorder.add_data((title, i.text, title, num))
#
#     # 查找下一页按钮（海象操作符）
#     if btn := tab('@rel=next', timeout=2):
#         # 如果有下一页，点击翻页
#         btn.click(by_js=True)
#         await asyncio.sleep(0.2)
#         await collect_data(tab, recorder, title, num + 1)
#
#
# async def main():
#     # 新建页面对象
#     browser = Chromium()
#     # 获取第一个标签页对象
#     tab1 = browser.latest_tab
#     tab1.get('https://gitee.com/explore/ai')
#     tab2 = browser.new_tab('https://gitee.com/explore/machine-learning')
#     # 新建记录器对象
#     recorder = Recorder('data.csv')
#     task1 = asyncio.create_task(collect_data(tab1,recorder,'ai'))
#     task2 = asyncio.create_task(collect_data(tab2,recorder,'机器学习'))
#
#     await task1
#     await task2
#
# if __name__ == '__main__':
#     asyncio.run(main())


# from DrissionPage import ChromiumPage, ChromiumOptions
# from bit_api import *
#
#
# path = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# co = ChromiumOptions().set_browser_path(path)

# browser_id = "2db6ec7b6f6e463da59e0ca32155d7f8" # 窗口ID从窗口配置界面中复制，或者api创建后返回
# res = openBrowser(browser_id)
# co = ChromiumOptions().set_browser_path(res["data"]['http'])

# 默认情况下，程序使用 9222 端口 浏览器可执行文件路径为'chrome'
# page = ChromiumPage(co).latest_tab # 创建对象
# page.get('https://book.douban.com/tag/小说?start=0&type=T')
# for _ in range(2): # 爬取2页
#     for book in page.eles('x://li[@class="subject-item"]'): # 遍历一页中所有图书
#         book_name = book.ele('x://h2/a').attr('title') # 获取书名
#         img = book('x://img') # 获取封面图片对象
#         img.save(path='./img/', name=f"{book_name}.png") # 保存图片
#         print("图片字节获取 img.src()", book_name, ) # 图片字节获取 img.src()
#         # 点击下一页
#     page('后页>').click()
#     page.wait.load_start()
# ------------------------------
#
# import asyncio
# from DrissionPage import ChromiumPage
# from DataRecorder import Recorder
# from DrissionPage._base import chromium
# from DrissionPage._configs.chromium_options import ChromiumOptions
# from TimePinner import Pinner
#
#
# async def collect_data(tab, recorder, title, num=1):
#     # 遍历所有标题元素并记录到记录器
#     for i in tab.eles('.title project-namespace-path'):
#         recorder.add_data((title, i.text, title, num))
#         # 查找下一页按钮（海象操作符）
#         if btn := tab('@rel=next', timeout=2):
#             # 如果有下一页，点击翻页
#             btn = tab('@rel=next', timeout=2)
#             btn.click(by_js=True)
#             await asyncio.sleep(0.2)
#             await collect_data(tab, recorder, title, num + 1)
#
#
# async def main():
#     # 新建页面对象
#     path = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
#     co = ChromiumOptions().set_browser_path(path)
#     browser = ChromiumPage(co)
#     # 获取第一个标签页对象
#     tab1 = browser.latest_tab
#     tab1.get('https://gitee.com/explore/ai')
#     # 新建一个标签页并访问另一个网址
#     tab2 = browser.new_tab('https://gitee.com/explore/machine-learning')
#     # 新建记录器对象
#     recorder = Recorder('data.csv')
#
#     task1 = asyncio.create_task(collect_data(tab1, recorder, 'ai'))
#     task2 = asyncio.create_task(collect_data(tab2, recorder, '机器学习'))
#
#     await task1
#     await task2
#
#
# if __name__ == '__main__':
#     pinner = Pinner()
#     pinner.pin()
#     asyncio.run(main())
#     pinner.pin('记录1')

# ----------------------------------

# from DrissionPage import Chromium
#
# # 启动或接管浏览器，并创建标签页对象
# tab = Chromium().latest_tab
# # 跳转到登录页面
# tab.get('https://gitee.com/login')
#
# # 定位到账号文本框，获取文本框元素
# ele = tab.ele('#user_login')
# # 输入对文本框输入账号
# ele.input('13337674154')
# # 定位到密码文本框并输入密码
# tab.ele('#user_password').input('123.chen')
# # 点击登录按钮
# tab.ele('@value=登 录').click()

# ----------------------------------
#
# from DrissionPage import SessionPage
#
# # 创建页面对象
# page = SessionPage()
#
# # 爬取3页
# for i in range(1, 4):
#     # 访问某一页的网页
#     page.get(f'https://gitee.com/explore/all?page={i}')
#     # 获取所有开源库<a>元素列表
#     links = page.eles('.title project-namespace-path')
#     # 遍历所有<a>元素
#     for link in links:
#         # 打印链接信息
#         print(link.text, link.link)

# ----------------------------------
from DrissionPage import Chromium
# 连接浏览器并获取一个Tab对象
tab = Chromium().latest_tab
# 访问网址
tab.get('https://gitee.com/explore/all')
# 切换到收发数据包模式
tab.change_mode()
# 获取所有行元素
items = tab.ele('.ui relaxed divided items explore-repo__list').eles('.item')
# 遍历获取到的元素
for item in items:
    # 打印元素文本
    print(item('t:h3').text)
    print(item('.project-desc mb-1').text)
    print()
