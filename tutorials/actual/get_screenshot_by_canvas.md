---
id: get_shot
title: '🥪 通过html2canva 获取某个元素的高清截图'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

此示例演示如何使用run_js通过html2canvas 获取某个元素的高清截图的功能。

## ✅️️ 页面分析

目标网址：

- https://www.doc88.com/p-781472637589.html?s=rel&id=3




---

## ✅️️ 编码思路

虽然 Dp库提供元素截图的功能，但是对于一些可以缩放的元素，元素放大超过视口的时候，截图效果会出现截图不全（超过视口的部分会截图不到）利用html2canvas库可以完美解决这个问题，可获取元素的高清截图。

使用`ChromiumPage`的`run_js()`方法，先载入html2canvas库，然后把canvas转换成img数据，保存到新建的img标签，然后对img标签进行保存。

---

## ✅️️ 示例代码

以下代码可直接运行。
**html2canvas 是异步函数，所以采用自动等待的语法等待其生成对应的img元素，然后再进行后续操作，但也可以把Python改成异步函数，可以直接接受run_js的返回值（这是第二种思路，代码逻辑略微复杂，暂时不提供示例）**

。

```python
# -*- coding:utf-8 -*-

#-导入库
from DrissionPage import Chromium, ChromiumOptions
# 导入类型判断
from DrissionPage.items import ChromiumTab,ChromiumElement

#-配置类
class Config:
    url='https://www.doc88.com/p-781472637589.html?s=rel&id=3'
    port=7878


#-创建配置对象
co=ChromiumOptions()

#-启动配置
co.set_local_port(Config.port)
co.ignore_certificate_errors(True)

#-创建浏览器
tab = Chromium(addr_or_opts=co).latest_tab
tab.get(Config.url)

element=tab.ele('#pageContainer')

# 通过canvas标签对元素进行高清截图
def get_shot_by_canvas( tab: ChromiumTab, ele: ChromiumElement, name='shot.png'):
    load_code = r"""
                function getShot_by_canvas() {
                    //加载库
                    if (!document.getElementById('html2canvas_id')) {
                        var script = document.createElement('script');
                        script.src = 'https://cdn.bootcdn.net/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
                        script.id = 'html2canvas_id';
                        document.body.appendChild(script);
                    }
                }
                getShot_by_canvas();
            """
    shot_code = r"""
        //截图
        html2canvas(this).then(function (canvas) {
            var img = canvas.toDataURL("image/png");
            var shot_img = document.createElement('img');
            shot_img.src = img;
            shot_img.id = 'shot_img';
            shot_img.style.visibility = 'hidden';  // 设置 visibility 为 hidden
            document.body.appendChild(shot_img);
        });
        """
    #加载HTML2canvas库
    tab.run_js(load_code)
    tab.wait.eles_loaded('#html2canvas_id')
    tab.wait(2)
    #运行截图代码，并等待异步函数在后台生成对应的img截图元素，截图元素内容越多等待时间就越长
    ele.run_js(shot_code)
    if img:=tab.ele('#shot_img',timeout=20):
        img.save(name=name)
        tab.remove_ele(img)
    

if __name__ =='__main__':

    #开始截图
    get_shot_by_canvas(tab,element,name='shot.png')

```

---

## ✅️️ 结果

程序生成一个结果图片文件 shot.png，内容如下：

![示例图片](https://wxhzhwxhzh.github.io/saossion_code_helper_online/img/shot.png)

---


