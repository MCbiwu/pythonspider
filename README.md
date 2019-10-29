## 爬虫代码库
***一个存放爬虫代码的仓库***
### 项目一：maoyan_top100:
 猫眼网站top100排行榜的爬虫代码，最基本的一个爬虫项目，使用request和正则表达式获取数据，保存为txt文本；
#### tip1:需要安装的依赖库
* import request
* import re
### 项目二：糗事百科
> 糗事百科网站目前维护
该项目使用scrapy框架来爬取数据，一些比较简单的代码；
#### tip1:依赖库
``` python
pip install scrapy
pip install pypiwin32
```
 如果在Windows系统上还需要安装pypiwin32依赖库
#### tip2:文件说明
``` python
spiders #爬虫代码文件
itens.py #封装数据文件
middlewares.py #中间件文件
piplines.py #下载器文件
settings.py #配置文件
start.py #配置文件
```
