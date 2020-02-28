#!/usr/local/bin/python3
#加减法数学游戏
#1.模式
# 1+1等于：2
# 回答正确!
# 是否继续?(y/n)y
# 1+2等于:1
# 错了，请继续!
# 1+2等于:3
# 回答正确!
# 是否继续?(y/n)n
# Bye-bye!

from random import randint,choice

# def add(x,y):
#     return x+y
#
# def sub(x,y):
#     return x-y
#
# def cheng(x,y):
#     return x*y

# def chu(x,y):
#     return x/y

def exam():
    #用于出题
    cmds={'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y}

    #随机选出两个数字
    nums=[randint(1,100) for i in range(2)]

    #降序排列
    #nums.sort()升序
    #nums.reverse()翻转
    nums.sort(reverse=True)

    #随机选出加减法
    # op=choice('+-')
    op=choice('+-*')

    #做出正确答案
    # if op=='+':
    #     result=nums[0]+nums[1]
    # else:
    #     result=nums[0]-nums[1]
    result=cmds[op](*nums)

    #要求用户做答,并判断
    counter=0 #计数器用于记录用户做答次数
    prompt='%s %s %s 等于:' %(nums[0],op,nums[1])
    while counter<3:
        try:
            answer=int(input(prompt))
        except(KeyboardInterrupt,EOFError):
            print('%s%s' % (prompt, result))
            break
        except(ValueError):
            print()
            continue
        if answer==result:
            print('回答正确!')
            break
        print('错了，请继续!')
        counter+=1
    else:
        print('%s%s' %(prompt,result))

def main():
    #主程序

    while 1:
        exam()
    #将用户输入的字符串去掉两端空格后,取第一个字符
        try:
            yn=input('是否继续?(y/n)').strip()[0]
        except(KeyboardInterrupt,EOFError):
            yn='n'
        except(IndexError):
            continue
        if yn in 'nN':
            print('Bye-bye!')
            break

if __name__ == '__main__':
    main()