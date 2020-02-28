#!/usr/local/bin/python3
# 解析enumerate()
# >>> s='python'
# >>> s
# 'python'
# >>> len(s)
# 6
#
# >>> for i in range(len(s)):
# ...     print(i,s[i])
# ...
# 0 p
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n
# >>> for i,j in enumerate(s):
# ...     print(i,j)
# ...
# 0 p
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

#列表
#属于容器,顺序,可变类型
# >>> l1=[10,20,30,10,15,8]
# >>> len(l1)
# 6
# >>> l1[-1]=80
# >>> l1
# [10, 20, 30, 10, 15, 80]
# >>> l1[6]=100
#报错,无法通过下标增加值
# >>> l1[1:3]=[1,2,3,4] 下标为1,2的元素
# >>> l1
# [10, 1, 2, 3, 4, 10, 15, 80]
# >>> l1.append(10)
# >>> l1
# [10, 1, 2, 3, 4, 10, 15, 80, 10]
# >>> l1.insert(2,80) 下标为2的位置插入80
# >>> l1
# [10, 1, 80, 2, 3, 4, 10, 15, 80, 10]
# >>> l1.extend([10,20,30])
# >>> l1
# [10, 1, 80, 2, 3, 4, 10, 15, 80, 10, 10, 20, 30]
# >>> l1.remove(1) 把列表中出现的第一个1删除,没有返回值,默认返回None
# >>> l1.remove(0)
# 报错
# >>> l1.pop(8) 把下标为8的项删掉,有返回值
# 80
# >>> l1
# [10, 80, 2, 3, 4, 10, 15, 10, 10, 20, 30]
# >>> l3=[1,2,3,4,5,6]
# >>> l3.pop() 从末尾开始向前删
# 6
# >>> a=l1.remove(10)
# >>> print(a)
# None
# >> l1.index(10) 第一个10的下标
# 0
# >>> l1.index(10,2) 从下标为2位置开始查找10的下标
# 6
# >>> l1.count(10) 统计有几个10
# 4
# >>> l1.sort() 升序排序
# >>> l1
# [2, 3, 4, 10, 10, 10, 15, 20, 30, 80]
# >>> l1.reverse() 翻转列表
# >>> l1
# [80, 30, 20, 15, 10, 10, 10, 4, 3, 2]
# >>> l3=l1.copy() 复制,使用不同内存地址
# >>> l3
# [80, 30, 20, 15, 10, 10, 10, 4, 3, 2]
# >>> l3.clear() 清空
# >>> l3
# []
# >>> l1
# [80, 30, 20, 15, 10, 10, 10, 4, 3, 2]

#元组
#属于容器,序列,不可变类型
#单元素元组,数据项后面必须有逗号,否则它不表示元组
# >>> t1=(10,)
# >>> t2=(10)
# >>> type(t1)
# <class 'tuple'>
# >>> type(t2)
# <class 'int'>
# >>> len(t1)
# 1
# >>> t1 元组
# (10,)
# >>> t2 数字
# 10
#元组的方法
# >>> t1.<tab><tab>
# t1.count(  t1.index(

#字典
#属于容器,可变,映射类型
# >>> d1={'name':'tom','age':20}
# >>> d1
# {'name': 'tom', 'age': 20}
# >>> d2=dict(['ab',(10,20),['email','tom@tedu.cn']])
# >>> d2
# {'a': 'b', 10: 20, 'email': 'tom@tedu.cn'}
# >>> d3=dict(['abcd'])
# 报错,len('ab')必须是2
# >>> dict([('name','tom'),('age',20),('email','tom@tedu.cn')])
# {'name': 'tom', 'age': 20, 'email': 'tom@tedu.cn'}
# 为字典的每个key添加相同的value
# >>> d3={}.fromkeys(['tom','jerry','bob','alice'],'man')
# >>> d3
# {'tom': 'man', 'jerry': 'man', 'bob': 'man', 'alice': 'man'}

#通过key来访问字典的value
# >>> d1
# {'name': 'tom', 'age': 20}
# >>> len(d1) 求长度
# 2
# >>> 'tom' in d1 'tom'是字典的key吗?
# False
# >>> 'name' in d1
# True
# >>> d1['name']
# 'tom'
# >>> for k in d1:
# ...     print('%s:%s' %(k,d1[k]))
# ...
# name:tom
# age:20
#字典的key不能重复,通过key进行赋值时,如果key已在字典中,则更新value,key不再字典中是增加新项
# >>> d1['age']=22
# >>> d1
# {'name': 'tom', 'age': 22}
# >>> d1['email']='tom@tedu.cn'
# >>> d1
# {'name': 'tom', 'age': 22, 'email': 'tom@tedu.cn'}
# >>> hash(10)
# 10
# >>> hash('abc')
# -154329884880667773
# >>> hash((1,2,3))
# 2528502973977326415
#hash(列表/字典)报错
# #字典的key必须使用不可变对象
# >>> d4={1:'aaa','name':'tom',(10,20):'jerry'}
# >>> d4
# {1: 'aaa', 'name': 'tom', (10, 20): 'jerry'}
#元组作为key的情况:坐标,棋盘...

#字典的常用方法
# >>> d1.
# d1.clear(       d1.get(         d1.pop(         d1.update(
# d1.copy(        d1.items(       d1.popitem(     d1.values(
# d1.fromkeys(    d1.keys(        d1.setdefault(

#get是字典最重要的方法
# >>> d1.get('name') 在d1中取出name对应的值
# 'tom'
# >>> d1['name']
# 'tom'
# >>> print(d1.get('qq')) d1中没有qq这个key,默认返回None
# None
# >>> d1.get('age','not found') 在字典中取出age对应的值,没有age返回not found
# 22
# >>> d1.get('qq','not found') 在字典中取出qq对应的值,没有qq返回not found
# 'not found'

# keys,values,items,pop方法
# >>> d1.keys()
# dict_keys(['name', 'age', 'email'])
# >>> list(d1.keys())
# ['name', 'age', 'email']
# >>> d1.values()
# dict_values(['tom', 22, 'tom@tedu.cn'])
# >>> list(d1.values())
# ['tom', 22, 'tom@tedu.cn']
# >>> d1.items()
# dict_items([('name', 'tom'), ('age', 22), ('email', 'tom@tedu.cn')])
# >>> list(d1.items())
# [('name', 'tom'), ('age', 22), ('email', 'tom@tedu.cn')]
# >>> d1.pop() 无序,报错
# >>> d1.pop('email')
# 'tom@tedu.cn'
# >>> d1
# {'name': 'tom', 'age': 22}
# >>> help(d1.popitem) 查帮助
# >>> d1.popitem() 随机弹出某一项
# ('age', 22)
# >>> d1
# {'name': 'tom'}
# >>> d1.update({'age': 22,'email': 'tom@tedu.cn'})
# >>> d1
# {'name': 'tom', 'age': 22, 'email': 'tom@tedu.cn'}

#集合
#由不同元素构成的数据类型
#集合元素不能重复
#集合元素必须是不可变对象
#集合没有顺序
#集合就像一个无值的字典,所以也使用{}表示

# >>> s1={10,20,'tom','jerry'}
# >>> type(s1)
# <class 'set'>
# >>> len(s1)
# 4
# >>> 10 in s1
# True
# >>> 'o' in s1
# False
# >>> for data in s1:
# ...   print(data)
# ...
# jerry
# 10
# tom
# 20
#证明无序

# 集合常用的操作
# >>> s1 = set('abc')
# >>> s2 = set('bcd')
# >>> s1
# {'b', 'c', 'a'}
# >>> s2
# {'b', 'c', 'd'}
# >>> s1 & s2    # 取交集
# {'b', 'c'}
# >>> s1 | s2    # 取并集
# {'c', 'd', 'b', 'a'}
# >>> s1 - s2    # 差补，在s1中有但s2中无的元素
# {'a'}
# >>> s2 - s1
# {'d'}
#集合常用的场景是去重
# >>> from random import randint
# >>> nums=[randint(1,50)for i in range(20)]
# >>> nums
# [3, 20, 27, 16, 42, 37, 44, 19, 9, 28, 44, 13, 12, 25, 2, 25, 25, 25, 7, 6]
# >>> set(nums)
# {2, 3, 37, 6, 7, 9, 42, 44, 13, 12, 16, 19, 20, 25, 27, 28}
# >>> list(set(nums))
# [2, 3, 37, 6, 7, 9, 42, 44, 13, 12, 16, 19, 20, 25, 27, 28]

#集合方法
# >>> s1.
# s1.add(                          s1.issubset(
# s1.clear(                        s1.issuperset(
# s1.copy(                         s1.pop(
# s1.difference(                   s1.remove(
# s1.difference_update(            s1.symmetric_difference(
# s1.discard(                      s1.symmetric_difference_update(
# s1.intersection(                 s1.union(
# s1.intersection_update(          s1.update(
# s1.isdisjoint(
#
# >>> s1.intersection(s2) s1&s2
# {'b', 'c'}
# >>> s1.union(s2) s1|s2
# {'a', 'd', 'b', 'c'}
# >>> s1.difference(s2) s1-s2
# {'a'}
# >>> s1.add('hello') 加一个
# >>> s1
# {'b', 'hello', 'a', 'c'}
# >>> s1.update(s2) 批量添加
# >>> s1
# {'hello', 'a', 'd', 'b', 'c'}
# >>> s1.issuperset(s2) s1是s2的超集吗?
# True
# >>> s2.issubset(s1) s2是s1的子集吗?
# True