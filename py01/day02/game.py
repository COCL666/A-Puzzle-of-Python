#!/usr/local/bin/python3
#法一
# import random
# #计算机随机选择
# xuan=['石头','剪刀','布'] #使用变量，防止硬编码
# computer=random.choice(xuan)
#
# #获取用户的输入
# player=input('请出拳(石头/剪刀/布):')
#
# #输出人机的选择
# print('您：%s 计算机：%s' %(player,computer))
#
# #判断输赢
# if player=='石头':
#     if computer== '石头':
#         print('平局')
#     elif computer== '剪刀':
#         print('您赢了!')
#     else:
#         print('您输了，再来')
# elif player=='剪刀':
#     if computer== '石头':
#         print('您输了，再来')
#     elif computer== '剪刀':
#         print('平局')
#     else:
#         print('您赢了!')
# else:
#     if computer== '石头':
#         print('您赢了!')
#     elif computer== '剪刀':
#         print('您输了，再来')
#     else:
#         print('平局')

#法二
# import random
# test=['石头','剪刀','布']
# pc=random.choice(test)
# player=input('请出拳(石头/剪刀/布):')
# print('您:%s pc:%s' %(player,pc))
#
# print('平局') if player==pc else print('你赢了！') if (player=='石头' and pc=='剪刀') or (player=='剪刀' and pc=='布') or (player=='布' and pc=='石头') else print('你输了')
#结果1 if 判断条件 else 结果2 if 判断条件 else 结果3

#法三
# import random
# test=['石头','剪刀','布']
# pc=random.choice(test)
# player=input('请出拳(石头/剪刀/布):')
# print('您:%s pc:%s' %(player,pc))
# #定义人赢的情况
# win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# #判断
# if player==pc:
#     print('平局')
# elif [player,pc] in win_list:
#     print('你赢了！')
# else:
#     print('你输了')

#调优
import random
test=['石头','剪刀','布']
pc=random.choice(test)

prompt='''(0)石头
(1)剪刀
(2)布
请选择(0/1/2):'''
i=int(input(prompt))

player=test[i]

print('您:%s pc:%s' %(player,pc))
#定义人赢的情况
win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
#判断
if player==pc:
    print('\033[32;1m平局\033[0m')
elif [player,pc] in win_list:
    print('\033[31;1m你赢了！\033[0m')
else:
    print('\033[33;1m你输了\033[0m')