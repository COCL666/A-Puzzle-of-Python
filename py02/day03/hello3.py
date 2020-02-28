#!/usr/local/bin/python3
# hashlib模块
# 用于计算数据的哈希值。
# 哈希即hash的音译，它是一个单向加密的算法
# 1.给定相同的数据，一定可以得到相同的乱码
# 2.不能通过乱码反向推出原始数据
# 3.用于存储加密的密码，也可以用于计算文件的完整性
# import hashlib
# m=hashlib.md5(b'123456')
# print(m.hexdigest()) #123456的哈希值
# 数据量很大的时候，可以采用分批计算
# >>> m1 = hashlib.md5()
# >>> m1.update(b'12')
# >>> m1.update(b'34')
# >>> m1.update(b'56')
# >>> m1.hexdigest()
# 'e10adc3949ba59abbe56e057f20f883e'

# tarfile模块
# 实现tar包功能,压缩解压缩
# 压缩
# >>> import tarfile
# >>> tar=tarfile.open('/var/tmp/mytest.tar.gz','w:gz')
# >>> tar.add('/etc/security')
# >>> tar.add('/etc/hosts')
# >>> tar.close()
#  解压缩
# >>> tar = tarfile.open('/var/tmp/mytest.tar.gz')
# >>> tar.extractall(path='/var/tmp')  # 不指定解压位置,将会解到当前目录
# >>> tar.close()

# OOP
# OOP:面向对象的编程
# 类(Class):一个模具,用来描述具有相同的属性和方法的对象的集合
# 实例化:创建一个类的实例,类的具体对象
# 方法:类中定义的函数
# 对象:通过类定义的数据结构实例;对象包括两个数据成员(类变量和实例变量)和方法.
# >>> class Bear:   #定义类,class是关键字
# ...     pass
# ...
# >>> b1=Bear()     #创建实例
# >>> b1.name='熊大'
# >>> b1.size='L'
# >>> b1.name
# '熊大'
# >>> b1.size
# 'L'
# 一切皆对象
# >>> type(10)
# <class 'int'>
# >>> l=[]
# >>> type(l)
# <class 'list'>
# >>> l.
# l.append(   l.count(    l.insert(   l.reverse(
# l.clear(    l.extend(   l.pop(      l.sort(
# l.copy(     l.index(    l.remove(

# 组合
#

# 子类
#

# 多重继承
# 子类可以有多个父亲
# 子类的实例拥有所有类的方法
# 实例查找方法,顺序是自下向上,自左向右

# 特殊方法
# 在class中,为了实现其内部功能,它们拥有很多以双下划线开头和结尾的特殊方法
# dir可以查看对象属性
# >>> type(10)
# <class 'int'>
# >>> dir(10)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# __init__  创建实例时,自动调用的方法
# __str__   在打印,显示实例时,自动调用
# __call__  使实例可以像函数一样调用

# re模块
# import re
# >>> re.match('f..','food')
# <_sre.SRE_Match object; span=(0, 3), match='foo'>
# >>> re.match('f..','seafood') 从开头匹配
# >>> print(re.match('f..','seafood'))
# None
# search应用更多,可以在字符串任意位置匹配
# >>> m=re.search('f..','seafood')
# >>> m.group() 通过group方法取出匹配内容
# 'foo'
# search只匹配到第一个满足条件的字符串,findall匹配到全部,返回列表
# >>> re.findall('f..','seafood is food')
# ['foo', 'foo']
# finditer返回所有匹配对象的生成器
# >>> for m in re.finditer('f..','seafood is food'):
# ...     m.group()
# ...
# 'foo'
# 'foo'

# 字符串的切割方法,只能指定一个分隔符
# >>> s='hello-world-ni-hao.tar.gz'
# >>> s.split('-')
# ['hello', 'world', 'ni', 'hao.tar.gz']
# 正则的切割符,可以指定多个
# >>> re.split('-|\.',s)
# ['hello', 'world', 'ni', 'hao', 'tar', 'gz']

# 字符串的替换方法
# >>> s.replace('-','/')
# 'hello/world/ni/hao.tar.gz'
# >>> s
# 'hello-world-ni-hao.tar.gz' #字符串是不可变类型
# 正则表达式的替换
# >>> re.sub('-|\.','/',s)
# 'hello/world/ni/hao/tar/gz'
# >>> s
# 'hello-world-ni-hao.tar.gz'

# 当有大量匹配时,为了有更好的效率,可以将正则的模式先进行编译
# >>> patt=re.compile('f..') #编译
# >>> m=patt.search('seafood')
# >>> m.group()
# 'foo'
# >>> patt.findall('seafood is foo')
# ['foo', 'foo']