#!/usr/local/bin/python3
# 统计功能
# 函数表示
import sys


def tongji(test, xuan):
    '可以统计apache日志access.log文件中给定项目的次数'


def menu():
    '选择统计什么'
    prompt = print('''(0)客户端访问次数
(1)客户端特定浏览器访问次数
(2)退出
请选择(0/1/2):''')
    cmds={0:tongji,1:tongji}
    while 1:
        try:
            xuan = input(prompt)
        except(KeyboardInterrupt, EOFError):
            break
        except(ValueError):
            continue

        if xuan==2:
            break
    cmds[xuan]()
if __name__ == '__main__':
    # test=sys.argv[0] #给定日志文件
    menu()

# OOP表示
# class tongji:
#     def
