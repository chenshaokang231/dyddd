---
id: download
title: '⭐ 下载文件' 
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

DrissionPage 带一个简便易用的下载器，一行即可实现下载功能。

```python
from DrissionPage import SessionPage

url = 'https://www.baidu.com/img/flexible/logo/pc/result.png'
save_path = r'C:\download'

page = SessionPage()
page.download(url, save_path)
```
