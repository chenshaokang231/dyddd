# 1.登录账号，用session保持cookies
# 2.打开网页，监听响应接口，查找元素
# 3.下一页，选择器selector
# 4.详情页采集
# 5.存储数据到recoder,再一次性downloader，开启mongodb
# 6.开多线程，python开异步，多任务
# 7.写在docker上部署

# 导入 ChromiumOptions
# from DrissionPage import Chromium
# browser = Chromium()
# tab = browser.latest_tab
# tab.get('https://www.winshangdata.com/brandList')
# # 切换到收发数据包模式
# # tab.change_mode()
# # 获取所有行元素
# items =tab.eles('x://ul[@class="clearfix"]/li')
# print(items)

#
# from DrissionPage import SessionPage
#
# page = SessionPage()
# page.get('https://gitee.com/explore')
#
# # 获取包含“全部推荐项目”文本的 ul 元素
# ul_ele = page.ele('x://ul')
# # print(ul_ele)
# # 获取该 ul 元素下所有 a 元素
# titles = ul_ele.eles('tag:a')
#
# # 遍历列表，打印每个 a 元素的文本
# for i in titles:
#     print(i.text)


# # 导入 ChromiumOptions
# from DrissionPage import Chromium, ChromiumOptions
# # 创建浏览器配置对象，指定浏览器路径
# co = ChromiumOptions().set_browser_path(r'/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary')
# # 用该配置创建页面对象
# browser = Chromium(addr_or_opts=co)

# 浏览器多开
# from DrissionPage import Chromium, ChromiumOptions
#
# co = ChromiumOptions().auto_port()
#
# tab1 = Chromium(addr_or_opts=co).latest_tab
# tab2 = Chromium(addr_or_opts=co).latest_tab
#
# tab2.get('https://DrissionPage.cn')
# tab1.get('https://www.baidu.com')

# from DrissionPage import Chromium
# from DrissionPage.common import Settings
#
# Settings.singleton_tab_obj = False
# browser = Chromium()
# tab1 = browser.get_tab()
# tab2 = browser.get_tab()
# print(tab1.title, id(tab1))
# print(tab2.title, id(tab2))

# from DrissionPage import Chromium
#
# tab = Chromium().latest_tab
# tab.set.load_mode.eager()  # 设置为eager模式
# tab.get('https://DrissionPage.cn')

# from DrissionPage import Chromium
#
# tab = Chromium().latest_tab
# tab.set.load_mode.none()  # 设置加载模式为none
#
# tab.listen.start('api/getkeydata')  # 指定监听目标并启动监听
# tab.get('http://www.hao123.com/')  # 访问网站
# packet = tab.listen.wait()  # 等待数据包
# tab.stop_loading()  # 主动停止加载
# print(packet.response.body)  # 打印数据包正文

# from DrissionPage import Chromium
#
# tab = Chromium().latest_tab
# tab.get('https://www.baidu.com')
# # html = '<a href="https://DrissionPage.cn" target="blank">DrissionPage </a> '
# # ele = tab.add_ele(html, '#s-top-left', '新闻')  # 插入到导航栏
# # ele.click()
# # 用传入参数的方式执行 js 脚本显示弹出框显示 Hello world!
# tab.run_js('alert(arguments[0]+arguments[1]);', 'Hello', ' world!')


# from DrissionPage import Chromium
# import re
#
# tab = Chromium().latest_tab
# tab.get('https://gitee.com/explore/all')  # 访问网址，这行产生的数据包不监听
#
# tab.listen.start('order=starred')  # 开始监听，指定获取包含该文本的数据包
# for _ in range(2):
#     tab('@rel=next').click()  # 点击下一页
#     data_packet = tab.listen.wait()  # 等待并获取一个数据包
#     # print(data_packet.response.body)  # 打印数据包url
#     content = re.findall(r"title='.*?<",data_packet.response.body)


# tab.close()

# 导入
# from DrissionPage import SessionPage
# # 创建页面对象
# page = SessionPage()
# # 访问网页
# page.get('https://gitee.com/explore/all')
# # 在页面中查找元素
# items = page.eles('t:h3')
# # 遍历元素
# for item in items[:-1]:
#     # 获取当前<h3>元素下的<a>元素
#     lnk = item('tag:a')
#     # 打印<a>元素文本和href属性
#     print(lnk.text, lnk.link)


# from DrissionPage import Chromium
# from DrissionPage.common import Settings
#
# browser = Chromium()
# tab1 = browser.new_tab()
# tab2 = browser.new_tab()
#
# tab1.get('https://gitee.com/explore/all')
# tab2.get('https://gitee.com/explore/all')
# from DrissionPage import SessionPage
# from pymongo import MongoClient
#
# class MongoDBRecorder:
#     def __init__(self, uri, db_name, collection_name):
#         self.client = MongoClient(uri)
#         self.db = self.client[db_name]
#         self.collection = self.db[collection_name]
#
#     def add_data(self, data):
#         self.collection.insert_one(data)  # 插入单条数据
#
#     def close(self):
#         self.client.close()  # 关闭数据库连接
#
# def get_list(page, dbrecorder):
#     """获取一页信息并添加到记录器"""
#     p = SessionPage()  # 创建页面对象
#     url = f'https://gitee.com/explore/all?page={page}'
#     p.get(url)  # 访问页面
#     rows = p('.ui relaxed divided items explore-repo__list').eles('.item')
#     for row in rows:  # 遍历所有行
#         data = {  # 产生一行数据
#             'page': page,
#             'title': row('.title project-namespace-path').text,
#             'content': row('.project-desc mb-1').text,
#             'stars': row('.stars-count').text
#         }
#         dbrecorder.add_data(data)  # 把一条数据放入记录器
#         print(data)
# def main():
#     # 创建 MongoDBRecorder 实例并传入参数
#     d = MongoDBRecorder('mongodb://localhost:27017/', db_name='drissionpage', collection_name='集合1')
#     for i in range(1, 2):  # 遍历1页
#         get_list(i, d)
#     d.close()  # 关闭数据库连接
#
# if __name__ == '__main__':
#     main()


from DrissionPage import SessionPage
from DrissionPage import Chromium
from pymongo import MongoClient

class MongoDBRecorder:
    def __init__(self, uri, db_name, collection_name, cache_size=100):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.cache_size = cache_size
        self.buffer = []  # 用于缓存数据

    def add_data(self, data):
        self.buffer.append(data)  # 将数据添加到缓存
        if len(self.buffer) >= self.cache_size:
            self.flush()  # 如果缓存满了，写入数据库

    def flush(self):
        if self.buffer:
            self.collection.insert_many(self.buffer)  # 一次性插入缓存的数据
            print(f'写入数据库的记录数: {len(self.buffer)}')
            self.buffer.clear()  # 清空缓存

    def close(self):
        self.flush()  # 关闭之前先写入剩余数据
        self.client.close()  # 关闭数据库连接

def get_list(page, dbrecorder):
    """获取一页信息并添加到记录器"""
    # tab = Chromium().latest_tab
    p = SessionPage()
    url = f'https://gitee.com/explore/all?page={page}'
    p.get(url)  # 访问页面
    rows = p('.ui relaxed divided items explore-repo__list').eles('.item')
    for row in rows:  # 遍历所有行
        data = {  # 产生一行数据
            'page': page,
            'title': row('.title project-namespace-path').text,
            'content': row('.project-desc mb-1').text,
            'stars': row('.stars-count').text
        }
        dbrecorder.add_data(data)  # 把一条数据放入记录器
        print(data)

def main():
    # 创建 MongoDBRecorder 实例并传入参数
    d = MongoDBRecorder(uri='mongodb://localhost:27017/', db_name='drissionpage', collection_name='集合1', cache_size=50)  # 可以设置缓存大小
    for i in range(1, 5):  # 遍历1页
        get_list(i, d)
    d.close()  # 关闭数据库连接

if __name__ == '__main__':
    main()

