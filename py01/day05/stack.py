#!/usr/local/bin/python3
#用列表模拟栈结构(后进先出),功能(压栈:push,出栈:pop,查询:view)
#模拟交互:

# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): push
# 无效的选择，请重试。
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 2
# []
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 0
# data:
# 没有获取到数据
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 2
# []
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 0
# data: hello
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 0
# data: nihao
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 2
# ['hello', 'nihao']
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 1
# 从栈中，弹出: niaho
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 1
# 从栈中，弹出: hello
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 1
# 空栈
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 2
# []
# (0) push
# (1) pop
# (2) view
# (3) quit
# Please input your choice(0/1/2/3): 3
# Bye-bye


#功能函数,及实现:

stack = []

def push():
    '用于实现压栈功能'

    date=input('data:').strip()
    if date:
        stack.append(date)

def pop():
    '用以实现出栈功能'

    if stack:
        print('从栈中,弹出:%s' %stack.pop())
    else:
        print('\033[31;1m空栈\033[0m')

def view():
    '用于实现查询功能'

    print(stack)

def show_menu():
    '用于实现菜单，根据用户选择调用对应函数'

#     print('''(0) push
# (1) pop
# (2) view
# (3) quit''')
#     prompt='Please input your choice(0/1/2/3):)'
#
#     while 1:
#         hello=input(prompt).strip() #删除用户输入字符串两边的空格
#
#         if hello not in ['0','1','2','3']:
#             print('Invalid selection, please try again!')
#             continue
#
#         if hello == '0':
#             push()
#         elif hello == '1':
#             pop()
#         elif hello == '2':
#             view()
#         else:
#             print('Bye-bye!')
#             break

    #字典是容器类型,将函数保存到字典
    cmds={'0':push,'1':pop,'2':view}

    print('''(0) push
(1) pop
(2) view
(3) quit''')
    prompt='Please input your choice(0/1/2/3):)'

    while 1:
        hello=input(prompt).strip() #删除用户输入字符串两边的空格

        if hello not in ['0','1','2','3']:
            print('Invalid selection, please try again!')
            continue

        if hello=='3':
            print('Bye-bye!')
            break

        cmds[hello]() #cmds[0]()--->push(),直接调用函数

if __name__ == '__main__':
    show_menu()