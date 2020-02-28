#!/usr/local/bin/python3
# import getpass #导入getpass模块
#
# username=input('用户名：')
# password=getpass.getpass('密码：') #getpass函数，调用getpass模块的getpass函数:getpass.getpass
# #使密码不回显
#
# if  username=='bob' and password=='123456':
#     print('登陆成功!')
# else:
#     print('登录失败!')
import getpass
uname=input('username:')
upass=getpass.getpass('password:')

if uname=='bob' and upass=='123456':
    print('Successful landing')
else:
    print('Landing failure')
