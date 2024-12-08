from DrissionPage.common import configs_to_here,Settings
from DrissionPage import Chromium, ChromiumOptions
from DataRecorder import Recorder, DBRecorder
from DownloadKit import DownloadKit
# 全局设置
Settings.raise_when_ele_not_found = True
Settings.auto_handle_alert = True
# 1.配置ini 文件，dp_configs.ini
configs_to_here()
co = ChromiumOptions(ini_path=r'dp_configs.ini')
# 1.co配置，可以链式操作
# 2.使用系统浏览器用户目录，以便复用用户信息和插件
# co = ChromiumOptions().use_system_user_path()
# co = ChromiumOptions().new_env()
# co = ChromiumOptions().headless()
# co = ChromiumOptions().incognito()
# co = ChromiumOptions().ignore_certificate_errors()
# co = ChromiumOptions().no_imgs()
# 2.浏览器插件，根据作者的经验，把插件文件解压到一个独立文件夹，然后把插件路径指向这个文件夹，会比较稳定
# co.add_extension()
# co.add_extension(r'D:\SwitchyOmega')
# 2.多开浏览器，auto_port()支持多线程，但不支持多进程
co = ChromiumOptions().auto_port()
# 实现多个配置启动浏览器；指定要读取的ini文件路径，默认是configs.ini文件
# co = ChromiumOptions(ini_path=r'./config1.ini')
browser = Chromium(co)
tab = browser.latest_tab

# 3.多标签页协作
browser.new_tab()
# link.click.for_new_tab()
# 获取指定的标签页对象
browser.get_tab(1)
# 4.多例，多个 Tab 对象共同管理一个标签页，可关闭单例模式：
# Settings.singleton_tab_obj = False
# 实际上允许多个 Tab 对象同时操作一个标签页，每个负责不同的工作。
# 比如一个执行主逻辑流程，另外的监视页面，处理各种弹窗。
# 5.点击、拖拽和悬停，动作链操作验证码，第三方识别库
# ddddocr,cv2模型库

# 6.加载策略
tab.set.load_mode.normal()
tab.set.load_mode.eager()
tab.set.load_mode.none()
# none模式技巧，跟监听器配合，也可以跟页面特征配合，
# 可在获取到需要的数据包时，主动停止加载。stop_loading()
# 8.页面交互：点击元素，输入内容，监听接口，执行js脚本，监听控制台，列表选择,页面滚动，wait等待
# 设置不加载css文件
tab.set.blocked_urls('*.css*')
tab.run_js()
# 等待页面加载完毕,再执行js
tab.run_js_loaded()
# 以异步方式执行 js 代码
tab.run_async_js()
# 添加初始化脚本，在页面加载任何脚本前执行。
tab.add_init_js()
# 执行cdp命令
tab.run_cdp()
# 获取控制台信息
tab.console.start()
# 触发XHR请求
tab.scroll.to_bottom()
tab.scroll.to_see()
# wait主动等待
tab.wait.eles_loaded()

# 6.***监听接口***，
tab.listen.start("")
tab.listen.wait()
# 监听listen，有DataPacket对象；DataPacket对象有response对象，返回html静态文本；
DataPacket = tab.listen.wait()


# 1.获取元素是自动化的重中之重
# tab对象和元素对象，都可以查找元素对象，有链式写法
# 所有涉及获取元素的操作都可以使用定位语法，如ele()、actions.move_to()、wait.eles_loaded()、get_frame()等等。
# 获取父级元素，然后在它里面查找子元素
# 用xpath语法，容易记
tab('x://div').eles('x:/a')
# 特殊情况，iframe，frame，同域名，异域名
tab.get_frame()
# 静态方式查找，s_eles()把整个页面或动态元素转变成一个静态元素，再在其中获取下级元素或信息
# 只需要获取最高级的容器元素，静态转换一次，
tab('t:body').s_eles('t:a')
# 静态文本，用lxml解析一下，之后就可以用xpath提取元素；
# 4.这主要用于应付长期运行导致内存占用过高，断开连接可释放内存，然后重连继续控制浏览器
tab.disconnect()
tab.reconnect()

# 5.切换模式，收发数据包
# 切换模式是用来应付登录检查很严格的网站，
# 可以用浏览器处理登录，再转换模式用收发数据包的形式来采集数据
# d 模式用于控制浏览器，s 模式使用requests收发数据包
tab.change_mode()
# 实现了两者 api 的统一，cookies 的互通

# 6.SessionPage，是对 requests 和 lxml 进行封装实现的，是请求接口，收发数据包
# 传递控制权，

# 2.多线程，threading，pool;
# 用线程threading模块或者线程池concurrent.futures.Executor，多线程

# 3.异步携程并发

# 3.DataRecorder,存储数据库
r = Recorder('data.csv')
r.add_data('data')
# 强烈建议在程序结束时显式调用record()保存数据
r.record()
# DBRecorder是用来处理sql类型数据库，mongodb不能处理
d = DBRecorder(path='data.db', cache_size=500, table='table1')
# mongodb用这个类
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


d = MongoDBRecorder(uri='mongodb://localhost:27017/', db_name='drissionpage', collection_name='table1',
                    cache_size=100)  # 可以设置缓存大小

# 3.DownloadKit，下载文件，是基于requests库，看看有没有更好用的库；
# 多线程并发下载文件
d = DownloadKit()
# DownloadKit对象，获取失败的任务
d.get_failed_missions()
# add()方法会返回一个Mission对象，该任务对象可用于，查看任务信息和管理任务。
mission = d.add('https://dldir1.qq.com/qqfile/qq/TIM3.4.8/TIM3.4.8.22086.exe')
print(mission.id)  # 获取任务id
print(mission.rate)  # 打印下载进度（百分比）
print(mission.state)  # 打印任务状态
print(mission.info)  # 打印任务信息
print(mission.result)  # 打印任务结果