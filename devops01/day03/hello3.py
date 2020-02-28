#!/usr/local/bin/python3
# Ansible是一个配置管理和配置工具,类似于Chef,Puppet或Salt(python,17年)
# ansible走ssh协议,适用于当前程序员工作
# ansible由python语言编写

# 列出ansible版本
# [root@zl2 day03]# pip install ansible==
# Looking in indexes: http://mirrors.aliyun.com/pypi/simple/
# (from versions: 1.0, 1.1, 1.2, 1.2.1, 1.2.2, 1.2.3, 1.3.0, 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.4, 1.4.1, 1.4.2, 1.4.3, 1.4.4, 1.4.5, 1.5, 1.5.1, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.6, 1.6.1, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9, 1.6.10, 1.7, 1.7.1, 1.7.2, 1.8, 1.8.1, 1.8.2, 1.8.3, 1.8.4, 1.9.0.1, 1.9.1, 1.9.2, 1.9.3, 1.9.4, 1.9.5, 1.9.6, 2.0.0.0, 2.0.0.1, 2.0.0.2, 2.0.1.0, 2.0.2.0, 2.1.0.0, 2.1.1.0, 2.1.2.0, 2.1.3.0, 2.1.4.0, 2.1.5.0, 2.1.6.0, 2.2.0.0, 2.2.1.0, 2.2.2.0, 2.2.3.0, 2.3.0.0, 2.3.1.0, 2.3.2.0, 2.3.3.0, 2.4.0.0, 2.4.1.0, 2.4.2.0, 2.4.3.0, 2.4.4.0, 2.4.5.0, 2.4.6.0, 2.5.0a1, 2.5.0b1, 2.5.0b2, 2.5.0rc1, 2.5.0rc2, 2.5.0rc3, 2.5.0, 2.5.1, 2.5.2, 2.5.3, 2.5.4, 2.5.5, 2.5.6, 2.5.7, 2.5.8, 2.5.9, 2.5.10, 2.5.11, 2.5.12, 2.5.13, 2.5.14, 2.5.15, 2.6.0a1, 2.6.0a2, 2.6.0rc1, 2.6.0rc2, 2.6.0rc3, 2.6.0rc4, 2.6.0rc5, 2.6.0, 2.6.1, 2.6.2, 2.6.3, 2.6.4, 2.6.5, 2.6.6, 2.6.7, 2.6.8, 2.6.9, 2.6.10, 2.6.11, 2.6.12, 2.6.13, 2.6.14, 2.6.15, 2.6.16, 2.6.17, 2.6.18, 2.6.19, 2.6.20, 2.7.0.dev0, 2.7.0a1, 2.7.0b1, 2.7.0rc1, 2.7.0rc2, 2.7.0rc3, 2.7.0rc4, 2.7.0, 2.7.1, 2.7.2, 2.7.3, 2.7.4, 2.7.5, 2.7.6, 2.7.7, 2.7.8, 2.7.9, 2.7.10, 2.7.11, 2.7.12, 2.7.13, 2.7.14, 2.7.15, 2.7.16, 2.8.0a1, 2.8.0b1, 2.8.0rc1, 2.8.0rc2, 2.8.0rc3, 2.8.0, 2.8.1, 2.8.2, 2.8.3, 2.8.4, 2.8.5, 2.8.6, 2.8.7, 2.8.8, 2.9.0b1, 2.9.0rc1, 2.9.0rc2, 2.9.0rc3, 2.9.0rc4, 2.9.0rc5, 2.9.0, 2.9.1, 2.9.2, 2.9.3, 2.9.4, 2.9.5)
# 安装
# pip3 install ansible==2.7.2
# [root@zl2 day03]# ansible --version
# ansible 2.7.2

# 创建工作目录
# cd day03
# mkdir myansible
# cd myansible
# yum -y install sshpass
# vim ansible.cfg
# [default]
# inventory = hosts
# remote_user = root
# vim hosts
# [dbservers]
# 192.168.137.128
# [webservers]
# 127.0.0.1
# 收集密钥,使之不需要yes
# ssh-keyscan 127.0.0.1 192.168.137.128 >> ~/.ssh/known_hosts
# 测试ansible all -m ping -k
# 设置免密钥登陆
# ssh-keygen
# ssh-copy-id ip

# ansible应用
# 执行ansible任务的两大方式：
# 1.adhoc临时命令
# ansible 主机清单 -m 模块 -a 参数
# 2.playbook
# ansible-playbook xxx.yml

# 配置vim,方便书写yaml文件
# [root@localhost myansible]# echo 'autocmd FileType yaml setlocal sw=2 ts=2 et ai' >> ~/.vimrc
#
# vi中ctrl+n可以补全文中已出现的单词
# 写playbook并执行：
# vim http.yaml
# ---
# - name: configure dbservers
#   hosts: dbservers
#   task:
#   - name: install mariadb
#     yum:
#       name: mariadb-server
#       state: present
#   -name: start mariadb
#    service:
#     name: mariadb
#     state: started
#     enabled: yes
#
# - name: configure webservers
#   hosts: webservers
#   task:
#   - name: install httpd
#     yum:
#       name: httpd
#       state: present
#   -name: start httpd
#    service:
#     name: httpd
#     state: started
#     enabled: yes

# 检查playbook：
# ansible-playbook --syntax-check http.yaml
# 执行http.yaml：
# ansible-playbook http.yaml

# ansible 的 Python API 代码示例
# adhoc.py来自https://docs.ansible.com/ansible/2.7/dev_guide/developing_api.html#python-api-example
# 复制执行即可
# Ansible Documentation网址:https://docs.ansible.com

# 命名的元组
# 还是元组,元组的相关方法仍然可用
# 给每个元组的下标起名,可以通过下标的名字访问对应的值

# >>> from collections import namedtuple
# >>> user = namedtuple('user',['name','age','email','qq'])
# >>> tom = user('Tom Smith',20,'tom@tedu.cn','13435435')
# >>> type(tom)
# <class '__main__.user'>
# >>> tom[:2]
# ('Tom Smith', 20)
# >>> tom.name
# 'Tom Smith'
# >>> tom.qq
# '13435435'
# >>> len(tom)
# 4

# 如果ansible连接远程服务器时,使用的是普通用户,执行命令需要提权
# 做法如下：
# [root@localhost myansible]# vim ansible.cfg
# [defaults]
# inventory = hosts
# remote_user = tom
# [privilege_escalation]
# become = yes
# become_user = root
# become_method = sudo
# become_ask_pass = no

# 在远程主机配置sudo
# [root@localhost myansible]# visudo
# 在root    ALL=(ALL)   ALL下加上:
# tom     ALL=(ALL)   NOPASSWD: ALL

# 使用ansible-vault
# [root@localhost myansible]# cp /etc/passwd /tmp/
# [root@localhost myansible]# cat /tmp/passwd
# 加密
# [root@localhost myansible]# ansible-vault encrypt /tmp/passwd
# New Vault password: tedu.cn
# Confirm New Vault password: tedu.cn
# [root@localhost myansible]# cat /tmp/passwd
# 解密
# [root@localhost myansible]# ansible-vault decrypt /tmp/passwd
# Vault password:
# [root@localhost myansible]# cat /tmp/passwd

# ansible-cmdb插件
# 收集被管理的主机信息,将内容写到/tmp/nsd1909目录下
# [root@localhost myansible]# ansible all -m setup --tree /tmp/nsd1909
#
# 安装ansible-cmdb
# [root@localhost myansible]# pip3 install ansible-cmdb
#
# [root@localhost myansible]# which ansible-cmdb
# /usr/local/bin/ansible-cmdb
# [root@localhost myansible]# vim $(which ansible-cmdb)  # 修改第8行为以下内容
# PY_BIN=$(which python3)
#
# # 使用ansbile-cmdb分析/tmp/nsd1909目录下的文件，生成html网页
# [root@localhost myansible]# ansible-cmdb /tmp/nsd1909/ > /tmp/hosts.html
#
# # 查看页面
# [root@localhost myansible]# firefox /tmp/hosts.html &

# ansible 模块
# [root@zl2 myansible]# ansible-doc -l | wc -l
# 2080
# 官网:Module index --> ALL modules

# 系统模块目录
# /usr/local/lib/python3.6/site-packages/ansible/modules
# 自定义模块目录
# mkdir myansible/mymodules/
# 临时定义:
# [root@zl2 mymodules]# export ANSIBLE_LIBRARY=/root/PycharmProjects/devops01/day03/myansible/mymodules
# 永久:
# [root@zl2 mymodules]# echo 'export ANSIBLE_LIBRARY=/root/PycharmProjects/devops01/day03/myansible/mymodules' >> /etc/profile
# 写模块
# rcopy.py:cp文件
# download2.py:从网上下载