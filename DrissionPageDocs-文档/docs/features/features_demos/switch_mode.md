---
id: change_mode
title: '⭐ 模式切换' 
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

用浏览器登录网站，然后切换到 requests 读取网页。两者会共享登录信息。

```python
from DrissionPage import Chromium

# 创建页面对象
tab = Chromium().latest_tab  
# 访问个人中心页面（未登录，重定向到登录页面）
tab.get('https://gitee.com/profile')  

# 输入账号密码登录
tab.ele('@id:user_login').input('您的用户名')  
tab.ele('@id:user_password').input('您的密码\n')
tab.wait.load_start()

# 切换到 s 模式
tab.change_mode()  
# 登录后 session 模式的输出
print('登录后title：', tab.title, '\n')
```

**输出：**

```shell
登录后title： 个人资料 - 码云 Gitee.com
```