程序功能(理想中)
- 爬虫 爬取社区,论坛,公众号(先只爬百度社区)的有效信息
- 监控 实时监控每个爬虫的运行状态
- 管理 爬虫管理, 关键词管理, urls和过滤规则管理
- 关键词预警 使用正则匹配 关键词和有效信息
- 警告模块 邮件,手机


## 服务端

## 客户端目录结构
```
qspider
	 | - manage.py
     | - settings.py
     | - data_request.py
     | - data_screen.py
     | - data_save.py
     | - up_log.py
     | - down_ctl.py
     | - requrements.txt
     | - readme.md
```