---
id: gitee
title: '🥪 自动登录码云'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

此示例演示使用控制浏览器的方式自动登录 gitee 网站。

## ✅️️ 网页分析

网址：https://gitee.com/login

![](/img/login_gitee1.jpg)

按`F12`查看代码，可见两个输入框都可用`id`属性定位，如图所示。

![](/img/login_gitee2.jpg)

---

## ✅️️ 编码思路

有`id`属性的元素获取非常简单。两个输入框直接用`id`属性定位即可。  
登录按钮没有`id`属性，但可观察到它是第一个`value`属性为`'登 录'`的元素，用中文定位也可以增强代码可读性。

由于使用浏览器登录，这里用`Chromium`来控制浏览器。

---

## ✅️️ 示例代码

```python
from DrissionPage import Chromium

# 用 d 模式创建页面对象（默认模式）
tab = Chromium().latest_tab
# 跳转到登录页面
tab.get('https://gitee.com/login')

# 定位到账号文本框并输入账号
tab.ele('#user_login').input('您的账号')
# 定位到密码文本框并输入密码
tab.ele('#user_password').input('您的密码')

# 点击登录按钮
tab.ele('@value=登 录').click()
```

---

## ✅️️ 结果

登录成功。

![](/img/login_gitee3.jpg)
