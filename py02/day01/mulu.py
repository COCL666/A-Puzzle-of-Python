#!/usr/local/bin/python3
#递归查看目录

# os.walk()怎么写?
# import os
#
# def mulu(lujing):
#
#     a=''
#     b=''
#     mulu_zi=os.listdir(lujing)
#     for line in mulu_zi:
#         if os.path.isfile(line):
#             a=a+line
#         else:
#             b=b+line
#     mulu = ['lujing', [a], [b]]
#     return mulu
#
# if __name__ == '__main__':
#     mulu('/tmp/nsd1909')
#     print(mulu)

# import os
#
# path=input('目录:')
#
# for data in os.walk(path):
#     print('%s:' %data[0])
#     for zimulu in data[1]:
#         print('\033[34;1m%s\033[0m' %zimulu,end='\n')
#     for file in data[2]:
#         print(file,end='n')
#     print('\n')

import os

path=input('目录:')

for path, folders, files in os.walk(path):
    print('%s:' % path)
    for zimulu in folders:
        print('\033[34;1m%s\033[0m' % zimulu, end='\t')
    for file in files:
        print(file, end='\t')
    print('\n')
