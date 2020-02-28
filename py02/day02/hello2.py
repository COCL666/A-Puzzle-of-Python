#!/usr/local/bin/python3
#函数基础
#def语句
#函数定义时,不执行其中的代码
#函数定义的先后顺序无所谓
# >>> def func1():
# ...     print('in func1')
# ...     func2()
# ...
# >>> def func2():
# ...     print('in func2')
# ...
# >>> func1()
# in func1
# in func2

#函数的参数部分,直接给定一个名字,如arg,称作位置参数
#函数的参数部分,给定的形式像key=val这样,称作关键字参数
# >>> def func1(name,age):
# ...     print('%s is %s years old' %(name,age))
# ...
# >>> func1('tom',20) ok
# tom is 20 years old
# >>> func1(20,'tom') 语法正确,语义不对
# 20 is tom years old
# >>> func1(name='tom',age=20) ok
# tom is 20 years old
# >>> func1('tom',age=20) ok
# tom is 20 years old
# >>> func1(age=20,'tom')
# 报错,关键字参数必须在位置参数后
# >>> func1()
# 报错,参数太少
# >>> func1('tom',20,30)
# 报错,参数太多

#参数组
#在定义函数时,参数名前加上*,表示使用元组接受参数
# >>> def func1(*canshu):
# ...     print(canshu)
# ...
# >>> func1()
# ()
# >>> func1('tom')
# ('tom',)
# >>> func1('tom',20)
# ('tom', 20)
#在定义函数时,参数名前加上**,表示使用字典接受参数
# >>> def func2(**kw_canshu):
# ...     print(kw_canshu)
# ...
# >>> func2()
# {}
# >>> func2(name='tom')
# {'name': 'tom'}
# >>> func2(name='tom',age=20)
# {'name': 'tom', 'age': 20}

#调用函数时,在参数名前加*表示将序列拆开
# >>> def func3(x,y):
# ...     print(x+y)
# ...
# >>> l=[10,20]
# >>> t=(100,200)
# >>> func3(*l)
# 30
# >>> func3(*t)
# 300

# 调用函数时，在参数名前加**，表示把字典拆成key=val的形式
# >>> def func4(name, age):
# ...   print('%s is %s years old' % (name, age))
# ...
# >>> user = {'name': 'tom', 'age': 20}
# >>> func4(**user)   # func4(name='tom', age=20)
# tom is 20 years old

#匿名函数
#当函数只有一行代码时,可以通过关键字lambda创建匿名函数
# >>> def add(x,y):
# ...     return x+y
# ...
#以上函数可以改为以下形式
# >>> myadd=lambda x,y:x+y #x,y是参数,x+y的结果自动成为返回值返回,不用return
# >>> myadd(10,20) #调用函数
# 30

#filter函数
#它接受两个参数
#第一个参数是函数,该函数接受一个参数,返回值必须是真或假
#第二个参数是序列对象
#filter将序列中的每个值传给第一个函数,返回真保留,返回假过滤掉
# >>> from random import randint
#   # >>> def func1(x):
#   # ...     return True if x%2==1 else False
#   # ...
#   #>>> if __name__=='__main__':
# ...     nums=[randint(1,100) for i in range(10)]
# ...     print(nums)
# ...     result=filter(lambda x:return True if x%2==1 else False,nums)
# nums是序列对象
#   #lambda x:return True if x%2==1 else False匿名函数是func1(x)
# ...     print(list(result))
# ...
# [43, 58, 7, 53, 22, 9, 32, 42, 78, 41] 100以内输出十个整数
# [43, 7, 53, 9, 41] 取奇数

#map函数
#它接受两个参数
#第一个参数是函数
#第二个参数是序列对象
#filter将序列中的每个值传给第一个函数,执行后返回
# >>> nums=[randint(1,100) for i in range(10)]
# >>> print(nums)
# [47, 78, 92, 47, 38, 20, 72, 16, 67, 90]
# >>> result=map(lambda x:x+2,nums)
# >>> print(list(result))
# [49, 80, 94, 49, 40, 22, 74, 18, 69, 92]

#变量作用域
#在函数外面定义的变量,是全局变量,全局变量在声明开始到程序结束,一直可见可用
# >>> x=10
# >>> def func1():
# ...     print(x)
# ...
# >>> func1()
# 10
#函数内的变量是局部变量,只能在函数内部使用
# >>> def func2():
# ...     a=10
# ...     print(a)
# ...
# >>> func2()
# 10
# >>> a
#报错
#全局变量遮盖局部变量
# >>> x=10
# >>> def func3():
# ...     x='hello'
# ...     print(x)
# ...
# >>> func3()
# hello
# >>> x
# 10
# 使用global关键字在局部定义全局变量
# >>> x=10
# >>> def func4():
# ...     global x
# ...     x=100
# ...     print(x)
# ...
# >>> func4()
# 100
# >>> x
# 100

#偏函数
#使用functools模块中的partial功能,改造现有函数,将其中的某些参数固定,生成新函数
# >>> def add(a,b,c,d,e):
# ...     return a+b+c+d+e
# ...
# >>> add(10,20,30,40,5)
# 105
# >>> add(10,20,30,40,2)
# 102
# >>> add(10,20,30,40,8)
# 108
# >>> from functools import partial
# >>> myadd=partial(add,10,20,30,40) partial生成新函数myadd
# >>> myadd(5)
# 105
# >>> myadd(2)
# 102
# >>> myadd(8)
# 108
#
# >>> int('11001100',base=2) #字符串是2进制
# 204
# >>> from functools import partial
# >>> int2=partial(int,base=2) 改造int函数,将base=2固定下来,生成新函数,名为int2
# >>> int2('1100000')
# 96

#图形界面编程:import tkinter

#递归函数
#一个函数内部又包含了对自身的调用,就是递归函数
#数字阶乘是非常直观的递归
# 5!=5*4*3*2*1
# >>> def func(n):
# ...     if n==1:
# ...             return 1
# ...     else:
# ...             return n*func(n-1)
# ...
# >>> print(func(5))
# 120
# >>> 5*4*3*2*1
# 120

#生成器
#使用生成器表达式,与列表解析有一样的语法

#使用生成器函数,与普通函数不一样,生成器函数可以用yield关键字返回很多中间值
#生成器函数的代码不是一次全部执行完,遇到yield会产生中间值,并停在那里,下一次向生成器函数取值时,它将继续向下运行
# >>> def mygen():
# ...     yield 100
# ...     a=10+5
# ...     yield a
# ...     b=100+200
# ...     yield b
# ...
# >>> mg=mygen() 创建生成对象
# >>> mg
# <generator object mygen at 0x7f176d5dea98>
# >>> mg.__next__()
# 100
# >>> mg.__next__()
# 15
# >>> mg.__next__()
# 300
# >>> mg.__next__()
#报错StopIteration
#或
# >>> mg=mygen()
# >>> for i in mg:
# ...     print(i)
# ...
# 100
# 15
# 300

#模块
#import sys
#print(sys.path)
#模块导入时,将会到sys.path定义的路径下导入模块
#法一:sys.path.append('目录')添加自己的目录
#法二:
#自己编写的模块,可以使用PYTHONPATH环境变量定义
#终端:export PYTHONPATH=目录

#目录也可以当作一个特殊的模块,术语叫作包
# mkdir aaa
# echo 'hi = "hello world"' > aaa/hello.py
# cat aaa/hello.py
# hi = "hello world"
# python3
# >>> import aaa.hello
# >>> aaa.hello.hi
# 'hello world'

