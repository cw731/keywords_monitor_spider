# 任务模板

## 直接获取数据的一级模板

```
{
    'name':'',
    'info': '',
    'rule': {
             'rule_type': 'xpash',
             'rule_data': ''
        },
    'data': {
             'data_type': 'data',
             'data': 'redis',
        },
    'urls':[
    
    ],
}
```
- name 任务名称
- info 任务简介
- rule 解析方法和解析语句 (xpash ,re, css)
- data 数据类型和存储方式 (redis,file, sql, mongo)
- urls url列表


## 获取url的二级模板
```
{
    'name':'',
    'info': '',
    'rule': {
             'rule_type': 'xpash',
             'rule_data': ''
        },
    'data': {
             'data_type': 'urls',
             'data': 'redis',
             'url_rule':{
                 'rule_type': 'xpash',
                 'rule_data': ''
                },
        },
    'urls':[
    
    ],
}
```
- name 任务名称
- info 任务简介
- rule 解析方法和解析语句 (xpash ,re, css)
- data 数据类型和存储方式 当data_type = urls
    这时需要定义url_rule
- urls url列表