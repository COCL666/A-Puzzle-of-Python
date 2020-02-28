#!/usr/local/bin/python3
# 找到mima文件中有，但是passwd文件中没有的行
# [root@localhost day05]# cp /etc/passwd /tmp/
# [root@localhost day05]# cp /etc/passwd /tmp/mima
# [root@localhost day05]# vim /tmp/mima  # 修改，使之与/tmp/passwd有不一样的行
# >>> with open('/tmp/mima') as f1:
# ...   s1 = set(f1)   # 把文件每一行，放到集合中
# ...
# >>> with open('/tmp/passwd') as f2:
# ...   s2 = set(f2)
# >>> s1 - s2   # 取差补，即mima中有，passwd中没有的行
# {'how are you?\n', 'hello world!\n'}
# >>> with open('/tmp/a.txt', 'w') as f3:
# ...   f3.writelines(s1 - s2)
# [root@localhost day05]# cat /tmp/a.txt
# how are you?
# hello world!