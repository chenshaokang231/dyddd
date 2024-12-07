from DrissionPage import Chromium, ChromiumOptions

# 1.co配置，可以链式操作
# 2.使用系统浏览器用户目录，以便复用用户信息和插件
# co = ChromiumOptions().use_system_user_path()
# co = ChromiumOptions().new_env()
# co = ChromiumOptions().headless()
# co = ChromiumOptions().incognito()
# co = ChromiumOptions().ignore_certificate_errors()
# co = ChromiumOptions().no_imgs()
# 2.多开浏览器，auto_port()支持多线程，但不支持多进程
co = ChromiumOptions().auto_port()
# 实现多个配置启动浏览器；指定要读取的ini文件路径，默认是configs.ini文件
# co = ChromiumOptions(ini_path=r'./config1.ini')
browser = Chromium(co)
# 3.多标签页协作
browser.new_tab()
# link.click.for_new_tab()
# 获取指定的标签页对象
browser.get_tab(1)
# 4.多例，多个 Tab 对象共同管理一个标签页，可关闭单例模式：
# Settings.singleton_tab_obj = False
# 实际上允许多个 Tab 对象同时操作一个标签页，每个负责不同的工作。
# 比如一个执行主逻辑流程，另外的监视页面，处理各种弹窗。












