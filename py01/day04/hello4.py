#!/usr/local/bin/python3
#写一个配ip地址的程序ip.py

#系统管理模块
#ctrl+点击模块名--->进入某块文件

#shutil模块:用于执行与文件系统相关的命令;跨平台
# >>> import shutil
# >>> shutil.copy('/etc/hosts','/tmp/zhuji') #cp
# '/tmp/zhuji'
# >>> shutil.copy2('/etc/hosts','/tmp/zhuji2') #cp -p
# '/tmp/zhuji2'
# >>> shutil.copytree('/etc/security','/var/tmp/anquan') #cp -r
# '/var/tmp/anquan'
# >>> shutil.move('/var/tmp/anquan','/tmp/anquan2') #mv
# '/tmp/anquan2'
# >>> shutil.rmtree('/tmp/anquan2') #rm -rf
# >>> shutil.chown('/tmp/zhuji',user='cocl',group='cocl') #chown
#查看帮助
# >>> help(shutil)
# >>> help(shutil.chown)
# python标准库官方文档：https://docs.python.org/zh-cn/3.8/library/index.html

#subprocess模块:直接调用系统命令;无法跨平台,各平台命令不同;
# >>> import subprocess
# >>> subprocess.run('ls')
# hello4.py  ip.py
# CompletedProcess(args='ls', returncode=0)
# >>> subprocess.run('ls ~',shell=True) #使用shell解析，不然无法识别
# anaconda-ks.cfg       模板
# bao                   视频
# bin                   图片
# initial-setup-ks.cfg  文档
# nsd2019               下载
# PycharmProjects       音乐
# 公共                  桌面
# CompletedProcess(args='ls ~', returncode=0)

# >>> result=subprocess.run('ls ~',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# 'ls ~' ---> 要执行的命令
# shell=True ---> 在shell环境中运行命令
# stdout=subprocess.PIPE ---> 固定写法,用于将输出保存到stdout中
# stderr=subprocess.PIPE ---> 固定写法,用于将错误保存到stderr中

# >>> result
# CompletedProcess(args='ls ~', returncode=0, stdout=b'anaconda-ks.cfg\nbao\nbin\ninitial-setup-ks.cfg\nnsd2019\nPycharmProjects\n\xe5\x85\xac\xe5\x85\xb1\n\xe6\xa8\xa1\xe6\x9d\xbf\n\xe8\xa7\x86\xe9\xa2\x91\n\xe5\x9b\xbe\xe7\x89\x87\n\xe6\x96\x87\xe6\xa1\xa3\n\xe4\xb8\x8b\xe8\xbd\xbd\n\xe9\x9f\xb3\xe4\xb9\x90\n\xe6\xa1\x8c\xe9\x9d\xa2\n', stderr=b'')
# 以上为对象和其属性
# >>> result.
# result.args
# result.check_returncode(
# result.returncode
# result.stderr
# result.stdout
# >>> result.args
# 'ls ~'
# >>> result.returncode #$?返回值
# 0
# >>> result.stdout #b''
# b'anaconda-ks.cfg\nbao\nbin\ninitial-setup-ks.cfg\nnsd2019\nPycharmProjects\n\xe5\x85\xac\xe5\x85\xb1\n\xe6\xa8\xa1\xe6\x9d\xbf\n\xe8\xa7\x86\xe9\xa2\x91\n\xe5\x9b\xbe\xe7\x89\x87\n\xe6\x96\x87\xe6\xa1\xa3\n\xe4\xb8\x8b\xe8\xbd\xbd\n\xe9\x9f\xb3\xe4\xb9\x90\n\xe6\xa1\x8c\xe9\x9d\xa2\n'
# >>> result.stdout.decode() #将bytes转为str
# 'anaconda-ks.cfg\nbao\nbin\ninitial-setup-ks.cfg\nnsd2019\nPycharmProjects\n公共\n\n视频\n图片\n文档\n下载\n音乐\n桌面\n'
# >>> print(result.stdout.decode())
# anaconda-ks.cfg
# bao
# bin
# initial-setup-ks.cfg
# nsd2019
# PycharmProjects
# 公共
# 模板
# 视频
# 图片
# 文档
# 下载
# 音乐
# 桌面
# >>> result.stderr.decode()
# '' #无错误输出

#python语法风格

#链式多重赋值:
# >>> x=y=10
# >>> id(x)
# 9360768
# >>> id(y)
# 9360768
# >>> y=20
# >>> id(x)
# 9360768
# >>> id(y)
# 9361088 存储位置变了
# >>> y
# 20
# >>> x
# 10
# 数字不可变,字符串和元组也不可变；只有列表和字典可变.
# >>> l1=l2=[1,2,3]
# >>> id(l1)
# 140560263848136
# >>> id(l2)
# 140560263848136
# >>> l1
# [1, 2, 3]
# >>> l2
# [1, 2, 3]
# >>> l1.append(19)
# >>> id(l1)
# 140560263848136 存储位置没变
# >>> id(l2)
# 140560263848136
# >>> l1
# [1, 2, 3, 19]
# >>> l2
# [1, 2, 3, 19]

#多元赋值:
# >>> a,b=1,2
# >>> c,d='mn'
# >>> g,h=['tom','jerry']
# >>> a
# 1
# >>> b
# 2
# >>> c
# 'm'
# >>> d
# 'n'
# >>> g
# 'tom'
# >>> h
# 'jerry'

#变量互换:
# >>> t=a
# >>> a=b
# >>> b=t
# >>> a
# 2
# >>> b
# 1
#python写法:
# >>> a,b=b,a
# >>> a
# 1
# >>> b
# 2
# >>> id(a)
# 9360480
# >>> id(b)
# 9360512
# >>> a,b=b,a
# >>> id(a)
# 9360512
# >>> id(b)
# 9360480
# 实际是把存储指向换了

#合法标识符:
# 第一个字符字母或下划线;
# 剩下的字符可以是字母数字下划线;
# 大小写敏感.

#关键字:不能被替换
# >>> import keyword
# >>> keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#内建:不是关键字,可以覆盖,但视情况而定;
#内建函数(内置函数):官网手册
# >>> len
# <built-in function len> #len是函数
# >>> len('abcd')
# 4
# >>> len=100
# >>> len('abcd')
# 报错

#python模块布局:

# #!/usr/local/bin/python3 #解释器位置
# "文档字符串,用于help"
#
# import os #导入模块
# import shutil
# import string
#
# all_chs=string.ascii_letters+string.digits #全局变量定义
# debug=True
#
# class MyClass: #定义类
#     pass
#
# def my_func(): #定义函数
#     pass
#
# if __name__ == '__main__':
#     mc=MyClass()
#     my_func()

#编程思路
#1.思考程序的工作方式,交互式?非交互?
#2.分析程序有哪些功能,将这些功能编写成功能函数,形成程序的大体框架.
#3.编写代码的主体,按一定的规则调用相关函数
#4.编写每个具体的函数代码
#详见mkfile.py

#序列
#序列类型操作符

#内建函数
#list(iter)把可迭代对象(序列对象)转换为列表
#str(obj)把obj对象转换成字符串
#tuple(iter)把一个可迭代对象转换成一个元组

#序列对象相关函数
#len():返回长度
#reversed():翻转序列对象，返回一个新的翻转结果，不会改变原始对象
# >>> seq='python'
# >>> reversed(seq)
# <reversed object at 0x7f128b45b9e8>
# >>> for zhuan in reversed(seq):
# ...     print(zhuan)
# ...
# n
# o
# h
# t
# y
# p
# >>> list(reversed(seq))
# ['n', 'o', 'h', 't', 'y', 'p']
# >>> seq[::-1]
# 'nohtyp'
# >>> l=[0,1,2,3]
# >>> list(reversed(l))
# [3, 2, 1, 0]

#sorted():排序,返回排序后的列表，不会改变对象本身
# >>> sorted(seq) #按字符大小排序
# ['h', 'n', 'o', 'p', 't', 'y']
# >>> ord('a') #a的ascii码
# 97
# >>> ord('A')
# 65
# >>> ord('b')
# 98
# >>> l=[2,1,0,3]
# >>> sorted(l)
# [0, 1, 2, 3]

#enumerate():可同时得到下标和值
# >>> list(enumerate(seq))
# [(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
# >>> for data in enumerate(seq):
# ...     print(data)
# ...
# (0, 'p')
# (1, 'y')
# (2, 't')
# (3, 'h')
# (4, 'o')
# (5, 'n')
# >>> for i,zifu in enumerate(seq):
# ...     print(i,zifu)
# ...
# 0 p
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

#字符串

#格式化操作符
#基本形式:'' % ()
# >>> '' % ()
# ''
#如果''中的占位符只有一项,()可省略不写
#%s是将相应的数据转换成str替代它
#  >>> 'hello %s' % 'tom'
# 'hello tom'
# >>> '%s is %s years old' % ('tom',20)
# 'tom is 20 years old'
#%d是整数
# >>> '%s is %d years old' % ('tom',20)
# 'tom is 20 years old'
# >>> '%d is %d years old' % ('tom',20)
# 报错,tom不是数字
# >>> '%s is %d years old' % ('tom',20.5)
# 'tom is 20 years old'
#%f是浮点数,%.2f:保留两位小数;%6.2f:总宽度为6，小数位两位，宽度不足6，左侧补空格
#  >>> '%f' % (5/3)
# '1.666667'
# >>> '%.2f' % (5/3)
# '1.67'
# >>> '%6.2f' % (5/3)
# '  1.67'
# >>> len('%6.2f' % (5/3))
# 6

#对齐
# >>> '%10s%5s' %('name','age') #右对齐
# '      name  age'
# >>> '%-10s%-5s' %('name','age') #左对齐
# 'name      age  '

#转进制
# >>> '%#o' %10 #8进制
'0o12'
# >>> '%#x' %10 #16进制
# '0xa'

#>>> '%e' %12000 #科学计数法
# '1.200000e+04' #1.2乘以10的4次方

#字符串格式化,format函数:
# >>> '{} is {} years old'.format('tom','12')
# 'tom is 12 years old'
# >>> '{0[0]} is {0[1]} years old'.format(['tom',12])
# 'tom is 12 years old'

#原始字符串(真实字符串)
# >>> win_path='c:\temp\new.txt'
# >>> print(win_path) #打印时\t是tab,\n是回车
# c:      emp
# ew.txt
# >>> wpath=r'c:\temp\new.txt' #在字符串前加r
# >>> print(wpath)
# c:\temp\new.txt
# >>> wpath
# 'c:\\temp\\new.txt'
# >>> win_path='c:\\temp\\new.txt'
# >>> print(win_path)
# c:\temp\new.txt

#字符串方法
#strip用于去除字符串两端的空白字符
# >>> s1='\thello world\n'
# >>> s1.strip()
# 'hello world'
# >>> s1.lstrip() 去左端空白
# 'hello world\n'
# >>> s1.rstrip() 去右端空白
# '\thello world'
# >>> s2='hello world'
# >>> s2.upper() 小写转大写
# 'HELLO WORLD'
# >>> s3='HELLO WORLD'
# >>> s3.lower() 大写转小写
# 'hello world'
# >>> s2.center(50) 居中,默认空格填充
# '                   hello world                    '
# >>> s2.center(50,'*') *填充
# '*******************hello world********************'
# >>> s2.ljust(50,'*') 左对齐
# 'hello world***************************************'
# >>> s2.rjust(50,'*') 右对齐
# '***************************************hello world'
#方法列表
# >>> s1.
# s1.capitalize(    s1.join(
# s1.casefold(      s1.ljust(
# s1.center(        s1.lower(
# s1.count(         s1.lstrip(
# s1.encode(        s1.maketrans(
# s1.endswith(      s1.partition(
# s1.expandtabs(    s1.replace(
# s1.find(          s1.rfind(
# s1.format(        s1.rindex(
# s1.format_map(    s1.rjust(
# s1.index(         s1.rpartition(
# s1.isalnum(       s1.rsplit(
# s1.isalpha(       s1.rstrip(
# s1.isdecimal(     s1.split(
# s1.isdigit(       s1.splitlines(
# s1.isidentifier(  s1.startswith(
# s1.islower(       s1.strip(
# s1.isnumeric(     s1.swapcase(
# s1.isprintable(   s1.title(
# s1.isspace(       s1.translate(
# s1.istitle(       s1.upper(
# s1.isupper(       s1.zfill(


