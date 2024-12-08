---
id: async
title: '🥪 异步递归操作多标签页'

#asyncio,模块专注于套接字连接的并发非阻塞 IO。
#例如，如果你的 IO 任务是基于文件I/O, 数据库I/O的，那么 asyncio 可能不是最合适的选择，至少仅因为这一点。
#原因是协程比线程更轻量级，因此一个线程可以托管比进程可以管理的线程多得多的协程。
#例如，asyncio 可能允许成千上万，甚至更多的协程用于基于套接字的 IO，而 threading API 可能只有几百到低数千个线程。
#原文链接：https://blog.csdn.net/captain5339/article/details/141404072
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

此示例演示如何使用异步的方式控制一个浏览器的多个标签页进行采集。

## ✅️️ 页面分析

目标网址：

- https://gitee.com/explore/ai
- https://gitee.com/explore/machine-learning

按`F12`，可以看到每个标题元素的`class`属性均为`title project-namespace-path`，可批量获取。

---

## ✅️️ 编码思路

虽然 gitee 开源项目列表可以用 s 模式采集，但现在为了演示多标签页操作，还是使用浏览器进行操作。

使用`ChromiumPage`的`get_tab()`方法，分别获取两个标签页的对象，传入不同线程进行操作。

---

## ✅️️ 示例代码

以下代码可直接运行。
**采用异步的方式操作标签页，既可以到达多线程的操作速度，又可以避免多线程操作标签页容易造成标签页卡死的缺点，另外 collect_data（）方法采用递归方式 和海象操作符，优化代码逻辑，让代码更加简洁优雅.**

需要注意的是，这里用到记录器对象，详见[DataRecorder](https://drissionpage.cn/DataRecorderDocs/)。

```python
import asyncio
from DrissionPage import Chromium
from DataRecorder import Recorder


async def collect_data(tab, recorder, title, num=1):
    # 遍历所有标题元素并记录到记录器
    for i in tab.eles('.title project-namespace-path'):
        recorder.add_data((title, i.text, title, num))

    # 查找下一页按钮（海象操作符）
    if btn := tab('@rel=next', timeout=2):
        # 如果有下一页，点击翻页
        btn.click(by_js=True)
        await asyncio.sleep(0.2)
        await collect_data(tab, recorder, title, num + 1)

        
async def main():
    # 新建页面对象
    browser = Chromium()
    
    # 获取第一个标签页对象
    tab1 = browser.latest_tab
    tab1.get('https://gitee.com/explore/ai')
    # 新建一个标签页并访问另一个网址
    tab2 = browser.new_tab('https://gitee.com/explore/machine-learning')
    # 新建记录器对象
    recorder = Recorder('data.csv')
 
    task1=asyncio.create_task(collect_data(tab1, recorder, 'ai'))
    task2=asyncio.create_task(collect_data(tab2, recorder, '机器学习'))

    await task1
    await task2

if __name__ == '__main__':
    asyncio.run(main())

```

---

## ✅️️ 结果

程序生成一个结果文件 data.csv，内容如下：

```csv
机器学习,MindSpore/mindspore,1
机器学习,PaddlePaddle/Paddle,1
机器学习,MindSpore/docs,1
机器学习,scruel/Notes-ML-AndrewNg,1
机器学习,MindSpore/graphengine,1
机器学习,inspur-inna/inna1.0,1
ai,drinkjava2/人工生命,1
机器学习,MindSpore/course,1

后面省略。。。
```

---

## ✅️️ 说明

在这个示例里，其实`page`就是一个标签页对象，相当于`tab1`。

示例中创建`tab1`对象仅仅为了看起来更直观，其实用`page`取代`tab1`的位置完全可以。
