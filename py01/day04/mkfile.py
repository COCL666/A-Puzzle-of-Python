#!/usr/local/bin/python3

#*******************************************************
#编程思路
#1.思考程序的工作方式,交互式?非交互?

# [root@localhost day04]# python3 mkfile.py
# 文件名: /etc/hosts
# 文件已存在,请重试.
# 文件名: /
# 文件已存在,请重试.
# 文件名: /tmp/abc.txt
# 请输入文件内容,在单独的一行输入end表示结束.
# (end to quit)> Hello World!
# (end to quit)> chi le ma?
# (end to quit)> the end
# (end to quit)> end
# [root@localhost day04]# ls /tmp/abc.txt
# /tmp/abc.txt
# [root@localhost day04]# cat /tmp/abc.txt
# Hello World!
# chi le ma?
# the end

#2.分析程序有哪些功能,将这些功能编写成功能函数,形成程序的大体框架.

# def get_fname():
#     '用于获取文件名，返回一个不存在文件名'
#
# def get_content():
#     '用于获取内容，返回一个列表'
#
# def wfile(fname, content):
#     '需要文件名和内容作为参数，将内容写入文件'

#3.编写代码的主体,按一定的规则调用相关函数

# def get_fname():
#     '用于获取文件名,返回一个不存在文件名'
#
# def get_content():
#     '用于获取内容,返回一个结果'
#
# def wfile(fname, content):
#     '需要文件名和内容作为参数,将内容写入文件'
#
# if __name__ == '__main__':
#     fname=get_fname()
#     content=get_content()
#     wfile(fname,content)

#4.编写每个具体的函数代码

#*******************************************************

"创建文件,写入数据......,用于help"


import os

def get_fname():
    '用于获取文件名,返回一个不存在文件名'
    while 1:
        fname=input('文件名:')
        #os.path.exists(fname) 如果文件已存在返回True,不存在返回False
        if not os.path.exists(fname):
            break
        print('文件已存在,请重试!')

    return fname

def get_content():
    '用于获取内容,返回一个结果'
    content=[] #创建一个列表,用于存储用户输入内容

    print('请输入文件内容,在单独的一行输入end表示结束.')
    while 1:
        line=input('(end to quit)>')
        if line=='end':
            break
        #content.append(line+'\n')
        content.append(line)
    return content

def wfile(fname, content):
    '需要文件名和内容作为参数,将内容写入文件'
    with open(fname,'w') as fobj:
        fobj.writelines(content)
if __name__ == '__main__':
    fname=get_fname()
    content=get_content()
    content=['%s\n' % line for line in content]
    wfile(fname,content)

