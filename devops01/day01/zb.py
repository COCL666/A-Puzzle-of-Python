import os
import time

print('starting')

rc = os.fork()
if rc:
    print('父进程')
    time.sleep(60)
    print('父进程结束')
else:
    print('子进程')
    time.sleep(5)
    print('子进程结束')

#watch -n1 ps a
#查僵尸进程,杀僵尸进程要杀它的父进程