#!/usr/local/bin/python3
s1='hello'
for zifu in s1: #一个一个字符打印
    print(zifu)

users=['tom','jerry','bob'] #列表内元素打印
for name in users:
    print(name)

nums=(10,20,15) #元组内元素打印
for i in nums:
    print(i)

d1={'name':'tom','age':20} #字典内键打印
for k in d1:
    print(k,d1[k])

# >>> range(10) 只是一个对象，占空间少，不用不占空间
# range(0, 10)
# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(6,10))
# [6, 7, 8, 9]
# >>> list(range(6,10,2)) 步长值2
# [6, 8]
# >>> list(range(1,10,-1))
# []
# >>> list(range(10,0,-1))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in range(10):
    print(i)
