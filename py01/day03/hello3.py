#!/usr/local/bythin3
# 9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s' %(j,i,i*j),end='\t')
#     print()
# 乘法表进阶
# n=int(input('请输入打印位数:'))
# for i in range(1,n):
#     for j in range(1,i+1):
#         print('%s*%s=%s' %(j,i,i*j),end='\t')
#     print()
# 以上为两层循环

# python中一切皆对象,每种对象都有自己的方法!!!

# 文件
# 文件操作的三个步骤：打开，读写，关闭

# 打开：open()函数
# 文件模式  操作
# r       以读方式打开(文件不存在则报错)
# w       以写方式打开(文件存在则清空,不存在则创建)
# a       以追加模式打开(必要时创建新文件)
# r+      以读写模式打开(参见r)
# w+      以读写模式打开(参见w)
# a+      以读写模式打开(参见a)
# b       以二进制模式打开

# 补充：
# 字符编码：在计算机上存储字符时，都是以2进制0/1的方式存储，将一连串的01组合表示为一个字符
# 美国采用的字符编码ASCII码；西欧采用ISO-8859-1；中国采用GBK/GB2312/GB18030；
# 不同国家采用的编码方案不同，导致相同的01组合在不同国家代表不同字符，为了解决这个问题，使得某种01的组合只能代表一个字符
# ISO提出了万国码Unicode,常用的Unicode解决方案是utf-8
# utf-8是变长的，一个英文字符占8位，一个汉字占24位
# python中，字符有str类型和bytes类型，str就是各种字符，如英文或中文，bytes是字节，一个英文字符正好是一个字节，一个汉字是三个字节
# >>> s1='a'
# >>> s2='中'
# >>> type(s1)
# <class 'str'>
# >>> type(s2)
# <class 'str'>
# >>> s1.encode() 将str转为bytes，默认utf-8
# b'a' b表示bytes类型，一个英文字符正好一字节，就用字符本身表示
# >>> s2.encode() 一个汉字是3字节，转换成16进制数表示，\x表示16进制
# b'\xe4\xb8\xad'
# >>> bin(0xe4b8ad) 将16进制转为2进制，在磁盘上存'中'就是存这些2进制数
# '0b111001001011100010101101'
# >>> b2=s2.encode()
# >>> b2
# b'\xe4\xb8\xad'
# >>> b2.decode() 将bytes转为str
# '中'
# 在 ASCII 编码中,一个英文字母字符存储需要1个字节.在 GB 2312 编码或 GBK 编码中,一个汉字字符存储需要2个字节.在UTF-8编码中,一个英文字母字符存储需要1个字节,一个汉字字符储存需要3到4个字节.在UTF-16编码中,一个英文字母字符或一个汉字字符存储都需要2个字节(Unicode扩展区的一些汉字存储需要4个字节).在UTF-32编码中,世界上任何字符的存储都需要4个字节.

# 读写
# 读取文本文件:
# >>> f=open('/tmp/password') 文件不存在报错
# >>> f=open('/tmp/passwd') 默认以r方式打开
# >>> data=f.read() read默认读取全部内容，返回字符串
# >>> f.close()
# >>> print(data)
# root:x:0:0:root:/root:/bin/bash
# ......
#
# >>> f=open('/tmp/passwd')
# >>> data=f.read() 读取文件内容，赋值给data
# >>> data=f.read() 继续读取覆盖了之前的文件，但上一次已经读完，这次读取为空
# >>> f.close()
# >>> data
# ''
#
# >>> f=open('/tmp/passwd')
# >>> f.readline() 读一行
# 'root:x:0:0:root:/root:/bin/bash\n'
# >>> f.readline() 继续读一行
# 'bin:x:1:1:bin:/bin:/sbin/nologin\n'
# >>> f.readlines() 将剩余行全部读取出来，成为字符串列表
# ['daemon:x:2:2:daemon:/sbin:/sbin/nologin\n', ......]
# >>> f.readline() 因为以全部读完，再读取则没有数据
# ''
# >>> f.close()
#
# 最常用的读取文本文件的方法:使用for循环
# >>> f=open('/tmp/passwd')
# >>> for line in f:
# ...     print(line,end='')
# ...
# root:x:0:0:root:/root:/bin/bash
# bin:x:1:1:bin:/bin:/sbin/nologin
# ......
# >>> f.close()

# 读取非文本文件:
# >>> f=open('/tmp/aaa.jpg','rb') 需要以bytes方式打开
# >>> f.read(10) 读10字节
# b'\xff\xd8\xff\xe0\x00\x10JFIF'
# >>> f.close()

# 写入文本文件
# >>> f=open('/tmp/passwd','w') 文件不存在则创建,存在则清空
# >>> f.write('hello world \n') 系统会把数据写入缓存
# 13 写入了13字节
# >>> f.flush() 立刻同步缓存到磁盘;当数据量达到4k时,也会写入磁盘;关闭文件也会写入磁盘
# [root@zl2 day03]# cat /tmp/passwd
# hello world
#
# >>> f.writelines(['2nd line \n','3rd line \n']) 写入列表
# >>> f.close()
# >>>
# [root@zl2 day03]# cat /tmp/passwd
# 2nd line
# 3rd line

# 写入非文本文件
# >>> s1='武汉加油\n'
# >>> f=open('/tmp/wh.txt','wb')
# >>> f.write(s1)
# 报错,只能写入bytes类型,但s1是str类型
# >>> s1.encode()
# b'\xe6\xad\xa6\xe6\xb1\x89\xe5\x8a\xa0\xe6\xb2\xb9\n'
# >>> f.write(s1.encode())
# 13
# >>> f.close()
# [root@zl2 day03]# cat /tmp/wh.txt
# 武汉加油

# with语句
# 通过with语句打开文件,with语句结束时,文件自动关闭
# >>> with open('/tmp/passwd') as f:
# ...     f.readline()
# ...
# '2nd line \n'
# >>> f.readline()
# 报错,由于文件已关闭

# 移动文件指针
# 通过seek函数移动文件指针,它有两个参数:
# 第二个参数有三个取值:0->开头,1->当前位置,2->结尾
# 第一个参数是相对于第二个参数的偏移量
# [root@zl2 day03]# cat /tmp/passwd
# 2nd line
# 3rd line
# [root@zl2 day03]# python3
# Python 3.6.7 (default, Feb  8 2020, 09:36:52)
# >>> f=open('/tmp/passwd','rb')
# >>> f.tell() 总是返回文件指针相对于开头的偏移量
# 0
# >>> f.seek(8,0) 移动文件指针,从开头向后移动8字节
# 8
# >>> f.readline() 读取从文件位置到行尾
# b' \n'
# >>> f.seek(-1,2) 移动文件指针,从结尾向左移动1字节
# 19
# >>> f.read() 读取从指针位置到结尾
# b'\n'
# >>> f.seek(0,2)
# 20
# >>> f.read()
# b''

# 重要:读取文件方法必须熟练掌握的有:
# 文本文件采用for循环;
# 非文本文件采用while循环,参见cp.py文件拷贝代码

# 函数
# 函数就是一堆代码集合,方便重复使用.

# 函数返回值
# 函数处理完数据后,往往有一个结果,这个结果可以使用return进行返回,如果没有return语句,那么它默认返回None.
# >>> def add():
# ...     result = 10 + 20 局部变量,在函数内定义,在函数内使用
# ...
# >>> a = add()
# >>> print(a)
# None 没有return默认None
#
# >>> def add():
# ...     a=10+5
# ...     b=2*3
# ...     return 'hello world'
# ...
# >>> r=add()
# >>> r
# 'hello world'

# 函数参数:
# 定义函数时,写在函数名后面括号中的内容称作形式参数.因为定义参数时,参数的值不确定,只是形式上占个位置,所以称作形式参数,简称形参;
# 调用函数时,需要将具体的数据传给函数,这个具体的数据是实际使用的参数,叫做实际参数,简称为实参.
# def mk_fib(n):
# ......
# nums=[5,8,10,20]
# for i in nums:
#   print(mk_fib(i)) #传参时,把i代表的数字传给mk_fib()函数,不是传变量
# a=mk_fib()

# 位置参数:
# 在python中,位置参数保存在sys模块的argv列表中,sys.argv[1]==$1

# 默认参数:
# 给定了默认值的参数
# >>> def pstar(n=30)
# ...     print('*' * n)
# ...
# >>> pstar() 没传参,默认30个*
# ******************************
# >>> pstar(5) 5个*
# *****

# 模块:getpass,sys,random,import......
# 模块是python从逻辑上组织代码的形式,文件python是从物理上组织代码的形式;
# 把文件的py扩展名去除,剩余部分及为模块名

# 导入模块的方法:
# >>> import sys 导入一个模块
# >>> from random import randint,choice 导入模块的部分方法
# >>> randint(1,100)
# 25
# >>> choice('abcd')
# 'd'
# >>> import getpass as gp 为模块取别名
# >>> passwd=gp.getpass()
# Password:
# >>> passwd
# '123'
# >>> import time,sys 一个import语句,导入多个模块
# 导入自己写的模块,及导入文star.py--->import star
# >>> import star
# >>> star.
# star.hi      star.pstar(
# >>> star.hi
# 'hello world'
# >>> star.pstar(5)
# *****

#模块的加载
#导入模块的时候,将会把模块内的代码执行一遍,这叫做加载load
#同一模块不管导入import多少次,只以第一次为准

#模块的特殊属性_name_
#它是python模块自带属性
#__name__是一个变量,这个变量在不同情况下有如下的两个值:
#模块直接运行时,值是__main__
#模块被导入时,值是模块名
# echo 'print(__name__)' > foo.py
# echo 'import foo' > bar.py
# cat foo.py
# print(__name__)
# cat bar.py
# import foo
# python3 foo.py
# __main__ 直接运行
# python3 bar.py
# foo 模块导入
#用法:main-->tab-->if __name__=='__main__':
#star.py如下:
# !/usr/local/bin/python3
# hi = 'hello world'
# def pstar(n=30):
#     print('*' * n)
# if __name__ == '__main__':
#     print(hi)
#     pstar(n=30)
# python3 star.py
# hello world
# **************************************************
#以上说明:__name__ == '__main__'
# >>> import star
# >>> star.hi
# 'hello world'
# >>> star.__name__ #导入模块的话__name__== 'star'
# 'star'





