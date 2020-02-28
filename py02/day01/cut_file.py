#!/usr/local/bin/python3
# import time
# import subprocess
#
# t9=time.strptime('2019-05-15 9:00:00','%Y-%m-%d %H:%M:%S')
# t12=time.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')
#
# def cut_file():
#     time_quchu=subprocess.run("awk '{print $1" "$2}' /root/PycharmProjects/py02/day01/mylog.log",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#     time_qu=print(time_quchu.stdout.decode())
#     for t in time_qu:
#         t1 = time.strptime(t, '%Y-%m-%d %H:%M:%S')
#         if t9<=t1<=t12:
#             print(time_qu)
#
# if __name__ == '__main__':
#     cut_file()
#以上错误,原因time_qu值为空,time_quchu的输出并非字符串

import time

t9=time.strptime('2019-05-15 9:00:00','%Y-%m-%d %H:%M:%S')
t12=time.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')

with open('mylog.log') as fobj:
    for line in fobj:
        t=time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        # if t9<= t <t12:
        #     print(line,end='')
        # if t>=t9 and t<t12:
        #     print(line,end='')
        if t>t12:
            break
        if t>=t9:
            print(line,end='')
        #节约资源