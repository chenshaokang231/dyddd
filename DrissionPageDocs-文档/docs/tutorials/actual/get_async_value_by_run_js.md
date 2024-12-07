---
id: get_async_value
title: '🥪 通过run_js方法获取某个异步js函数的返回值'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

此示例演示如何使用通过run_js方法获取某个异步js函数的返回值。

## ✅️️ 页面分析

目标网址：

- https://m.weibo.cn/




---

## ✅️️ 编码思路

Dp库提供run_js（）方法，直接打通了python和js这两大语言之间的隔阂，很多网友不知道怎么接受异步js函数的返回值，这里通过示例代码简单说明。



---

## ✅️️ 示例代码

以下代码可直接运行。
**先编写好异步js代码，使用`ChromiumPage`的`run_js()`方法直接获取其fetch的返回值。**

。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

#-导入库
from DrissionPage import ChromiumPage,ChromiumOptions
# 导入类型判断
from DrissionPage.items import ChromiumTab,ChromiumElement

#-配置类
class Config:
    url='https://m.weibo.cn/'
    port=7878


#-创建配置对象
co=ChromiumOptions()

#-启动配置
co.set_local_port(Config.port)
co.ignore_certificate_errors(True)

#-创建浏览器
page = ChromiumPage(addr_or_opts=co)
tab=page.new_tab(Config.url)
js_code='''
// 异步函数，使用Fetch获取数据
async function fetchData() {
  try {
    // 使用Fetch API获取数据
    const response = await fetch('https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1076032145291155&page=2');
    
    // 确认请求成功
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    
    // 解析JSON格式的响应数据
    const data = await response.json();
    
    // 在控制台打印json数据
    
    console.log(data)
    // 返回json中的其中一条信息
    return data.data.cards[0].mblog.text;
  } catch (error) {
    // 捕获Fetch请求失败或者处理响应数据出错
    console.error('Error fetching data:', error);
    // 可以选择抛出异常或者返回一个默认值
    throw error;
  }
}

// 返回异步函数的返回值
return fetchData();

'''

if __name__ =='__main__':

    #开始
    response_txt=tab.run_js(js_code)
    print(response_txt)

```

---

## ✅️️ 结果

程序返回json数据中的一条信息，内容如下：


>马云公益基金会和阿里巴巴公益基金会对非洲的第二批捐赠已经出发！这批紧急医疗防疫物资包括500台呼吸机、100万套病毒采样设备和提取试剂，20万套防护服和防护面罩，2000个额温枪和 50万双手套，我们用最快的速度发往54个非洲国家。再次感谢埃塞俄
比亚总理阿比，感谢您还有埃塞俄比亚航空公司、非洲疾 ...<a href="/status/4490697220163703">全文</a>
---


