#!/usr/local/bin/python3
import subprocess
import time
import os


def ping(host):
    result = subprocess.run('ping -c2 %s &>/dev/null' % host, shell=True)
    if result.returncode == 0:
        print('%s:up' % host)
    # else:
    #     print('%s:down' % host)


if __name__ == '__main__':
    ips = ['192.168.137.%s' % i for i in range(1, 255)]
    print(time.ctime())
    # start=time.time()
    for ip in ips:
        #     ping(ip)
        # 多进程
        rc = os.fork()
        if not rc:
            ping(ip)
            exit()
        # for l in range(len(ips)):
        #     os.waitpid(-1, 0)
    # end=time.time()
    # print(end-start)
    print(time.ctime())
