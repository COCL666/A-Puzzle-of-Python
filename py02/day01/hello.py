#!/usr/local/bin/python3
#time模块
#时间表示方法:
#时间戳:自1970-1-1 0:00:00到某一时间点之间的秒数
#UTC时间:世界协调时,以英国格林威治这个城市所在的经度为基准,向东向西每15度角划分一个时区,全球共24个时区
#struct_time:九元组时间.年,月,日,时,分,秒,一周中的第几天,一年中的第几天,是否使用夏季节约时间
#索引     属性                  值
#0      tm_year                 2000
#1      tm_mon                  1-12
#2      tm_mday                 1-31
#3      tm_hour                 0-23
#4      tm_min                  0-59
#5      tm_sec                  0-61 闰秒
#6      tm_wday                 0-6(0为周一)
#7      tm_yday(一年中的第几天)   1-366
#8      tm_isdst(是否为dst时间)  默认为-1

#time模块的方法
#官方文档:https://docs.python.org/zh-cn/3/library/time.html
# >>> import time
# >>> time.time() 返回时间戳
# 1581730826.4441404
# >>> time.ctime() 返回当前的时间字符串
# 'Sat Feb 15 09:41:02 2020'
# >>> time.ctime(0) 时间戳为0秒时的当前时间
# 'Thu Jan  1 08:00:00 1970'
# >>> time.localtime()
# time.struct_time(tm_year=2020, tm_mon=2, tm_mday=15, tm_hour=9, tm_min=42, tm_sec=16, tm_wday=5, tm_yday=46, tm_isdst=0)
# >>> t=time.localtime()
# >>> type(t)
# <class 'time.struct_time'>
# >>> t.tm_year
# 2020
# >>> t.tm_yday
# 46
# >>> t.tm_wday
# 5
# >>> time.gmtime(0) 时间开始的点:epoch
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# >>> time.sleep(3) 睡眠3秒
# >>> time.strftime('%Y-%m-%d %a %H:%M:%S')
# '2020-02-15 Sat 10:20:42'
# >>> time.strptime('2020-2-14 12:00:00','%Y-%m-%d %H:%M:%S')
# time.struct_time(tm_year=2020, tm_mon=2, tm_mday=14, tm_hour=12, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=45, tm_isdst=-1)
# 转化成九元组时间可比大小
# >>> t1=time.strptime('2020-2-14 12:00:00','%Y-%m-%d %H:%M:%S')
# >>> t2=time.strptime('2020-1-14 12:00:00','%Y-%m-%d %H:%M:%S')
# >>> t1>t2
# True

#datetime模块
# >>> import datetime
# >>> datetime.datetime.now()
# datetime.datetime(2020, 2, 15, 11, 6, 42, 953533)
#以上太麻烦
# >>> from datetime import datetime
# >>> t=datetime.now() 返回当前
# >>> t.year,t.month,t.day,t.hour,t.minute,t.second
# (2020, 2, 15, 11, 7, 19)

# >>> t.strftime('%Y-%m-%d %H:%M:%S') 转换成字符串
# '2020-02-15 11:07:19'
#将时间字符串转换为datetime对象
# >>> t=datetime.strptime('2020-02-15 11:07:19','%Y-%m-%d %H:%M:%S')
# >>> t
# datetime.datetime(2020, 2, 15, 11, 7, 19)

#异常
#异常就是不正常,当程序遇到各种各样错误时,程序将会崩溃,终止执行
#异常处理就是提前想到程序可能出现的错误

# 异常处理语法格式:
# try:
    # 有可能发生异常的代码
# except 异常1:
    # 异常发生则输出
# except 异常2 as 变量:
    # 异常发生则输出格式如:print('错误:',变量),输出异常报错
# else:
    # 不发生异常才执行的代码
# finally:
    # 不管异常是否发生,一定会执行

#触发异常
#通过raise关键字,抛出异常
#通过assert关键字,抛出AssertionError

#os模块
#os模块是python访问文件系统主要采用的模块
#os模块的方法
# os.<tab><tab>
# Display all 319 possibilities? (y or n)

# >>> os.listdir() #'ls'
# ['.idea', 'timejia.py', 'mylog.log', 'cut_file.py', 'mydiv.py', 'get_info.py', 'hello.py']
# >>> os.listdir('/tmp') #'ls /tmp'
# ['yum.log', 'hsperfdata_root', '.font-unix', '.XIM-unix', '.ICE-unix', '.Test-unix', '.X11-unix', 'ks-script-se4sPn', 'firefox_root', 'wh.txt', 'yum_save_tx.2020-02-12.21-42.MHu2qi.yumtx', '+~JF2206857536719971201.tmp', 'yum_save_tx.2020-02-10.09-03.jN2Auw.yumtx', 'user.txt', 'yum_save_tx.2020-02-12.22-05.wreIIp.yumtx', 'anaconda.log', 'storage.log', 'program.log', 'packaging.log', 'sensitive-info.log', 'ifcfg.log', '.esd-990', 'yum_save_tx.2020-02-12.09-21.k7MP23.yumtx', 'yum_save_tx.2020-02-12.22-09.2XJ7am.yumtx', 'zhuji', 'abc.txt', 'yum_save_tx.2020-02-12.22-07.jX8Wm6.yumtx', '.esd-1000', 'passwd', 'yum_save_tx.2020-02-15.09-04.qu499J.yumtx', '+~JF7076278129314900538.tmp', '+~JF5327382839361923059.tmp', 'tracker-extract-files.1000', 'VMwareDnD', 'yum_save_tx.2020-02-11.09-03._eWkSB.yumtx', 'systemd-private-696ddb08000b4089a9b09a72967a8203-cups.service-tGAjh2', '+~JF8539941994141460787.tmp', 'touch', 'zhuji2', '.X0-lock', 'systemd-private-696ddb08000b4089a9b09a72967a8203-colord.service-C6n2nZ', '.esd-0', 'tracker-extract-files.0', 'yum_save_tx.2020-02-07.22-08.oslBam.yumtx', 'systemd-private-696af1fffde84d84b0d6367efbb777c5-chronyd.service-uRjD77', 'systemd-private-696af1fffde84d84b0d6367efbb777c5-rtkit-daemon.service-QFQjOz', 'yum_save_tx.2020-02-12.21-53.v6D7Km.yumtx', 'systemd-private-696af1fffde84d84b0d6367efbb777c5-cups.service-4Fo6fy', 'yum_save_tx.2020-02-12.21-51.TUfBVN.yumtx', 'systemd-private-696af1fffde84d84b0d6367efbb777c5-colord.service-c24BKH', 'ssh-AbWcpYTWi2gk', 'vmware-root', 'systemd-private-696ddb08000b4089a9b09a72967a8203-chronyd.service-C96fjN', 'ssh-nSJSaq7dE5yo', '+~JF7584884874182952246.tmp', 'yum_save_tx.2020-02-12.22-01.1D06bE.yumtx', 'systemd-private-696ddb08000b4089a9b09a72967a8203-rtkit-daemon.service-bYymEt', '+~JF123034356846225480.tmp', 'yum_save_tx.2020-02-14.08-33.ol4COh.yumtx', '+~JF8305377656355051461.tmp', '+~JF6150335627366764648.tmp', '+~JF685031405442450394.tmp', 'yum_save_tx.2020-02-12.21-42.vbDRTD.yumtx', '+~JF5263570637458581010.tmp', 'mozilla_root0', 'yum_save_tx.2020-02-12.22-25.wQUtus.yumtx', 'aaa.jpg']

# >>> os.mkdir('/tmp/nsd1909') #'mkdir /tmp/nsd1909'
# >>> os.makedirs('/tmp/nsd1909/aaa/bbb/ccc') #'mkdir -p /tmp/nasd1909/aaa/bbb/ccc'

# >>> os.chdir('/tmp/nsd1909') #'cd /tmp/nsd1909'
# >>> os.getcwd() #'pwd'
# '/tmp/nsd1909'

# >>> os.mknod('hi.txt') #'touch hi.txt'
# >>> os.listdir() #'ls'
# ['aaa', 'hi.txt']

# >>> os.symlink('/etc/hosts','zhuji') #'ln -s /etc/hosts zhuji'软连接

# >>> os.remove('hi.txt') 删除文件
# >>> os.listdir()
# ['aaa', 'zhuji']

# >>> os.mknod('hello.txt')
# >>> os.listdir()
# ['aaa', 'zhuji', 'hello.txt']
# >>> os.chmod('hello.txt',0o755)#linux权限是8进制数要加0o表示8进制

# >>> os.getcwd()
# '/tmp/nsd1909'
# >>> os.listdir()
# ['aaa', 'zhuji', 'hello.txt']
# >>> os.mkdir('abc')
# >>> os.listdir()
# ['aaa', 'zhuji', 'hello.txt', 'abc']
# >>> import shutil
# >>> shutil.copy('/etc/hosts','abc')
# 'abc/hosts'
# >>> shutil.copy('/etc/passwd','abc')
# 'abc/passwd'
# >>> os.mkdir('ccc')
# >>> os.mknod('aaa/a.txt')
# >>> os.mknod('aaa/b.txt')
# >>> os.mknod('aaa/bbb/b1.txt')
# >>> os.mknod('aaa/bbb/b2.txt')
# >>> os.mknod('ccc/c2.txt')
# >>> os.mknod('ccc/c1.txt')

# [root@zl2 ~]# ls -R /tmp/nsd1909
# .:
# aaa  abc  ccc  hello.txt  zhuji
#
# ./aaa:
# a.txt  bbb  b.txt
#
# ./aaa/bbb:
# b1.txt  b2.txt  ccc
#
# ./aaa/bbb/ccc:
#
# ./abc:
# hosts  passwd
#
# ./ccc:
# c1.txt  c2.txt

# >>> list(os.walk('/tmp/nsd1909'))
# [('/tmp/nsd1909', ['aaa', 'abc', 'ccc'], ['zhuji', 'hello.txt']),
# ('/tmp/nsd1909/aaa', ['bbb'], ['a.txt', 'b.txt']),
# ('/tmp/nsd1909/aaa/bbb', ['ccc'], ['b1.txt', 'b2.txt']),
# ('/tmp/nsd1909/aaa/bbb/ccc', [], []),
# ('/tmp/nsd1909/abc', [], ['hosts', 'passwd']),
# ('/tmp/nsd1909/ccc', [], ['c2.txt', 'c1.txt'])]

# >>> mulu=list(os.walk('/tmp/nsd1909'))
# >>> len(mulu)
# 6
# >>> mulu[1]
# ('/tmp/nsd1909/aaa', ['bbb'], ['a.txt', 'b.txt'])
# >>> mulu[2]
# ('/tmp/nsd1909/aaa/bbb', ['ccc'], ['b1.txt', 'b2.txt'])
# >>> mulu[3]
# ('/tmp/nsd1909/aaa/bbb/ccc', [], [])
# >>> mulu[4]
# ('/tmp/nsd1909/abc', [], ['hosts', 'passwd'])
# >>> mulu[5]
# ('/tmp/nsd1909/ccc', [], ['c2.txt', 'c1.txt'])
#经分析,mulu列表由6个元组构成,每个元组拥有一样的结构
#每个元组有三项内容:(字符串,列表1[文件夹],列表2[文件])
#字符串:目录路径

# >>> os.path.basename('/tmp/nsd2019/abc.txt') 文件
# 'abc.txt'
# >>> os.path.dirname('/tmp/nsd2019/abc.txt') 目录
# '/tmp/nsd2019'
# >>> os.path.split('/tmp/nsd2019/abc.txt') 切割路径
# ('/tmp/nsd2019', 'abc.txt')
# >>> os.path.join('/tmp/nsd2019', 'abc.txt') 路径拼接
# '/tmp/nsd2019/abc.txt'
# >>> os.path.isfile('/etc/hosts') 文件存在并且是文件吗?
# True
# >>> os.path.isdir('/etc/hosts') 存在并且是目录吗?
# False
# >>> os.path.islink('/etc/grub2.cfg') 存在并且是链接文件吗?
# True
# >>> os.path.ismount('/') 存在并且是挂载点吗?
# True
# >>> os.path.exists('/etc') 存在吗?
# True

#pickle模块
#文件默认只能写入str或bytes类型的数据
#
# >>> f=open('/tmp/a.txt','w')
# >>> f.write('hello')
# 5
# >>> f.write(100)
#报错
# >>> f.close()
# >>> f=open('/tmp/a.txt','wb')
# >>> f.write(100)
#报错
# >>> f.close()

# >>> gouwu=['方便面','速冻水饺','苹果']
# >>> import pickle
# >>> with open('/tmp/shop.data','wb') as fobj:
# ...     pickle.dump(gouwu,fobj) 将列表存入文件
# ...
# >>> with open('/tmp/shop.data','rb') as fobj:
# ...     l=pickle.load(fobj) 从文件中取出数据
# ...
# >>> l
# ['方便面', '速冻水饺', '苹果']
# >>> type(l)
# <class 'list'>

