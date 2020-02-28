#!/usr/local/bin/python3
#编写一个能生成8位随机密码的程序
#使用random的choice函数随机取出字符
#改进程序,用户可以自己决定生成多少位密码
import string,sys
from random import choice
from string import digits,ascii_letters
zifuji=digits+ascii_letters

def passwd(n=8):
    result=''
    for i in range(n):
        p=choice(zifuji)
        result+=p
    return result
if __name__ == '__main__':
    r=passwd()
    print(r)
    print(passwd(4))
