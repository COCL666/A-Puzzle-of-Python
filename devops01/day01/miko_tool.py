#!/usr/local/bin/python3

import paramiko
import threading


def miko_tool(ip, username, password, command):
    # 创建客户端实例
    ssh = paramiko.SSHClient()
    # 设置自动接受密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 登录服务器
    ssh.connect(ip, username=username, password=password)
    # 执行命令
    # result=ssh.exec_command(command)
    # 执行命令返回的值是一个3元素元组,这3项分别是输入,输出和错误的类文件对象,类文件对象提供了read方法,可以读取其中的内容
    stdin, stdout, stderr = ssh.exec_command(command)
    print('输出:', stdout.read())
    print('报错:', stderr.read())
    ssh.close()

if __name__ == '__main__':
    info=[('192.168.137.128','root','cocl:666','id root; id dingle'),('192.168.137.3','root','cocl:666','id root; id dingle')]
    # ips = ['192.168.137.128','192.168.137.3']
    # usernames = ['root','root']
    # passwords = ['cocl:666','cocl:666']
    # commands = ['id root; id dingle','id root; id dingle']
    for ip,username,password,command in info:
        t = threading.Thread(target=miko_tool, args=(ip, username, password, command))
        t.start()
