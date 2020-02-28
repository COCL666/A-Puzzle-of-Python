#!/usr/local/bin/python3
# 1.模拟：
#(0)注册
#(1)登陆
#(2)退出
#请输入(0/1/2):0

#注册
#新用户名：cocl
#用户名已被注册，请重新输入!

#新密码(8~12位)：***
#密码格式不正确,请重新输入!

#密码重复：****
#两次输入不同，请重新输入!

#新密码：***
#密码重复：***

#注册成功!

#请输入(0/1/2):1
#登陆
#用户名：
#密码：
#密码或用户名错误,请重新输入

#同一用户超过5次密码错误,帐户封停!

#登陆成功!

#请输入(0/1/2):2
#Bye-bye!

#2.功能
import getpass

userdb={}
userdb_err={}
username_err = []

def register():
    '用于注册新用户'

    while 1:
        username=input('新用户名:').strip()
        if not username or (username in userdb):
            print('用户名为空或已被注册，请重新输入!')
            continue
        break
    while 1:
        password=getpass.getpass('新密码(8~12位)：').strip()
        if len(password)<8 or 12<len(password):
            print('请输入8~12位新密码!')
            continue
        while 1:
            password_2=getpass.getpass('密码重复：').strip()
            if password_2!=password:
                print('两次输入不同，请重新输入!')
                continue
            break
        break
    userdb.update({username:password})
    print('注册成功!')

def login():
    '用于实现用户登录'

    while 1:
        username=input('用户名:').strip()
        password=getpass.getpass('密码：').strip()

        # if (username not in userdb) or (userdb[username]!=password):
        if (userdb.get(username)!=password) and (username not in userdb_err):
            username_err.append(username)
            print('密码或用户名错误,请重新输入!')
            if username_err.count(username)>4:
                userdb_err.update({username:password})
            continue
        elif username in userdb_err:
            print('同一用户名超过5次密码错误,帐户封停!')
            break
        else:
            print('登陆成功!')
            break


def show_menu():
    '用于打印菜单,根据用户选择调用相关函数'

    cmds={'0':register,'1':login}

    prompt='''(0)注册
(1)登陆
(2)退出
请选择(0/1/2):'''

    while 1:
        hello=input(prompt).strip()
        if hello not in ['0','1','2']:
            print('无效选择,请重试!')
            continue

        if hello=='2':
            print('Bye-bye!')
            break

        cmds[hello]()

if __name__ == '__main__':
    show_menu()