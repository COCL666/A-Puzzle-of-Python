#!/usr/local/bin/python3
#生成n位的斐波那契数列0 1 0+1 1+1 1+2 2+3 3+5 5+8......
fib=[0,1]
n=int(input('长度:'))
for i in range(n-2):
    fib.append(fib[-1]+fib[-2])
print(fib)
