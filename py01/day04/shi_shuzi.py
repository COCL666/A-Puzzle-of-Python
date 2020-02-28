#!/usr/local/bin/python3
#'123asd'.isdigit()  isdigit()方法,判断字符串是否全为数字
#False
def shi_shuzi():
    for zifu in s:
        if not zifu in '0123456789':
            print('不全是数字')
            break
    else:
        print('全是数字')

if __name__ == '__main__':
    s=input('number:')
    shi_shuzi(s)