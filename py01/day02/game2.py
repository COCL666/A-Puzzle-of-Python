#!/usr/local/bin/python3
#三局两胜
#法一
# import random
#
# test=['石头','剪刀','布']
# prompt='''(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2):'''
# win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# pwin=0 #人胜利的计数器
# cwin=0 #计算机胜利的计数器
#
# while pwin < 2 and cwin < 2:
#     pc=random.choice(test)
#
#     i=int(input(prompt))
#     player=test[i]
#
#     print('您:%s pc:%s' %(player,pc))
#
#     if player==pc:
#         print('\033[32;1m平局\033[0m')
#     elif [player,pc] in win_list:
#         print('\033[31;1m你赢了！\033[0m')
#         pwin += 1
#     else:
#         print('\033[33;1m你输了\033[0m')
#         cwin += 1
#法二
import random

test=['石头','剪刀','布']
prompt='''(0)石头
(1)剪刀
(2)布
请选择(0/1/2):'''
win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
pwin=0 #人胜利的计数器
cwin=0 #计算机胜利的计数器

while 1:
    pc=random.choice(test)

    i=int(input(prompt))
    player=test[i]

    print('您:%s pc:%s' %(player,pc))

    if player==pc:
        print('\033[32;1m平局\033[0m')
    elif [player,pc] in win_list:
        print('\033[31;1m你赢了！\033[0m')
        pwin += 1
    else:
        print('\033[33;1m你输了\033[0m')
        cwin += 1

    if pwin == 2 or cwin == 2:
        break
