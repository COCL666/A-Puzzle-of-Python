#!/usr/local/bin/python3
#异常处理语句
# try:
#     n=int(input('number:'))
#     result=100/n
#     print(result)
# except (ValueError,ZeroDivisionError) as e:#将报错信息保存到变量中
#     print('错误:',e)
# except (KeyboardInterrupt,EOFError):
#     print('\nbye')

# print('done')#没有异常处理时执行

try:
    n=int(input('number:'))
    result=100/n
except (ValueError,ZeroDivisionError) as e:#将报错信息保存到变量中
    print('错误:',e)
except (KeyboardInterrupt,EOFError):
    print('\nbye')
    exit() #程序遇到exit将会彻底结束
else: #异常不发生才执行的语句,放到else中
    print(result)
finally: #不管异常是否发生,一定会执行
    print('done')

