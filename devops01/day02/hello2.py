#!/usr/local/bin/python3
# 邮件
# 发送邮件使用SMTP协议,端口号25
# 准备邮件使用email模块
# 使用smtplib模块

# JSON
# JavaScript Object Notation
# json应用
# >>> import json
# >>> data={'name':'tom','age':20}
# 发送之前，需要将数据转换成json字符串
# >>> jdata=json.dumps(data)
# >>> type(jdata)
# <class 'str'>
# >>> jdata
# '{"name": "tom", "age": 20}'
# 接收到的数据，再通过loads转换成对应的数据类型
# >>> info=json.loads(jdata)
# >>> type(info)
# <class 'dict'>
# >>> info
# {'name': 'tom', 'age': 20}

# requests
# 是用python语言编写的,优雅而简单的HTTP库
# 内部采用urllib3
# HTTP最常用的方法：
# get:浏览器中输入url访问;页面中点击超链接;搜索引擎提交表单
# post:一般用于表单提交数据,比如登陆,注册
# request模块将每个HTTP的方法都创建出了对应的函数

# requests应用
# api:应用程序接口
# 中国天气网提供的接口
# 实况天气：http://www.weather.com.cn/data/sk/城市代码.html
# 城市信息：城市代码.html
# 详细指数：城市代码.html
# 城市代码通过网络搜索
# 101010100 北京
# 安装:pip3 install requests

# 文本形式的内容,使用text属性获取
# >>> import requests
# >>> url1='http://www.163.com'
# >>> r1=requests.get(url1)
# >>> r1.text

# 非文本数据,使用content属性获取,bytes类型.文本数据也可以使用此种方式
# >>> url2='https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3104074246,4054913645&fm=26&gp=0.jpg'
# >>> r2=requests.get(url2)
# >>> r2.content
# >>> with open('/tmp/a.jpg','wb') as fobj:
# ...     fobj.write(r2.content)
# [root@zl2 day02]# eog /tmp/a.jpg

# json数据,通过json()方法获取
# >>> url3='http://www.weather.com.cn/data/sk/101010100.html'
# >>> import requests
# >>> r3=requests.get(url3)
# >>> r3.json()
# {'weatherinfo': {'city': 'å\x8c\x97äº¬', 'cityid': '101010100', 'temp': '27.9', 'WD': 'å\x8d\x97é£\x8e', 'WS': 'å°\x8fäº\x8e3çº§', 'SD': '28%', 'AP': '1002hPa', 'njd': 'æ\x9a\x82æ\x97\xa0å®\x9eå\x86µ', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
# 乱码
# >>> r3.encoding
# 'ISO-8859-1'
# >>> r3.encoding='utf8' #修改编码
# >>> r3.json()
# {'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9', 'WD''南风', 'WS': '小于3级', 'SD': '28%', 'AP': '1002hPa', 'njd': '暂无实况', 'W, 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}

# 传参
# >>> kd_url='http://www.kuaidi100.com/query'
# >>> params={'type':'youzhengguonei','postid':'9893442769997'}
# >>> r=requests.get(kd_url,params=params)
# >>> r.json()
# {'message': 'ok', 'nu': '9893442769997', 'ischeck': '1', 'com': 'youzhengguonei', 'status': '200', 'condition': 'F00', 'state': '3', 'data': [{'time': '2020-02-17 14:59:00', 'context': '查无结果', 'ftime': '2020-02-17 14:59:00'}]}

# 修改请求头
# >>> js_url='http://www.jianshu.com'
# >>> r=requests.get(js_url)
# >>> r.text #403 forbidden
# >>> headers='User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
# >>> r=requests.get(js_url,headers=headers)
# >>> r.text #正常内容

