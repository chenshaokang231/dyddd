from DrissionPage import Chromium, ChromiumOptions

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
# 3.全局设置
tab.set.auto_handle_alert()
tab.set.blocked_urls('*.css*')
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
# 5.切换模式，收发数据包
# 切换模式是用来应付登录检查很严格的网站，
# 可以用浏览器处理登录，再转换模式用收发数据包的形式来采集数据
# d 模式用于控制浏览器，s 模式使用requests收发数据包
tab.change_mode()
# 6.cookies管理，SessionPage
# SessionPage,保持对话状态，保持cookies信息，可以从tab对象中提取session

# 6.加载策略
tab.set.load_mode.normal()
tab.set.load_mode.eager()
tab.set.load_mode.none()
# none模式技巧，跟监听器配合，跟页面特征配合，可在获取到需要的数据包时，主动停止加载。stop_loading()
# 8.页面交互：点击元素，输入内容，监听接口，执行js脚本，监听控制台，列表选择,页面滚动，wait等待
# 6.监听接口，
tab.listen.start("")
tab.listen.wait()
# 监听listen，有DataPacket对象；DataPacket对象有response对象，返回html静态文本；
DataPacket = tab.listen.wait()
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
# 2.DataRecorder,存储数据库

# 3.DownloadKit
# 多线程并发下载多个文件

# 4.这主要用于应付长期运行导致内存占用过高，断开连接可释放内存，然后重连继续控制浏览器
tab.disconnect()
tab.reconnect()


