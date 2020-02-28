#!/usr/local/bin/python3
#编写程序,用于改变ip地址,并自动检测ip是否冲突,若冲突会推荐可用ip范围
#1.工作方式
# >>> python3 ip.py
# 请输入网卡名和ip地址(eth0:192.168.137.3):
# 如果ip冲突--->'ip冲突,请重新配置!',并在下一次推荐可用ip范围;
# 不冲突则'ip:<192.168.137.3>,配置成功!'
#ip addr
#2.功能
# def get_ip():
    #获取网卡名和ip地址
# def check_ip():
    #检测ip冲突
# def mk_ip(ip):
    #修改ip
#3.主体

"说明......"


import os
import subprocess

def get_eth():
    eth=input('请输入网卡名:')
    while 1:
        if os.path.exists('/etc/sysconfig/network-scripts/ifcfg-'+eth):
            break
        else:
            eth = input('请输入网卡名:')
    return eth

def get_ip():
    ip = input('请输入ip地址:')
    ip_old = subprocess.run("ifconfig %s | awk '/inet/ {print $2}'" % eth, shell=True)
    while 1:
        if ip!=ip_old:
            break
        else:
            ip = input('请输入ip地址:')
    return ip

def mk_ip(eth,ip):
    subprocess.run('sed -i "/IPADDR/s/^.*$/IPADDR=%s/" /etc/sysconfig/network-scripts/ifcfg-%s' %(ip,eth), shell=True)
if __name__ == '__main__':
    eth=get_eth()
    ip=get_ip()
    mk_ip(eth,ip)