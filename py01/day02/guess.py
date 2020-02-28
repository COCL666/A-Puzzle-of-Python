#!/usr/local/bin/python3
#猜数字，7次机会，猜对不会输出正确答案，猜错7次输出正确答案
import random
num=random.randint(1,100)
i=0
while i<7:
    i+=1
    guess=int(input('猜数字(1~100):'))
    if  guess==num:
        print('猜对了')
        break #不执行循环的else
    elif guess>num:
        print('猜大了')
    else:
        print('猜小了')
else:
    print('答案是:%s' %num)
