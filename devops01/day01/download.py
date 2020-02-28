#!/usr/local/bin/python3
from urllib import request

url = 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=661409485,3554849204&fm=15&gp=0.jpg'
fname = '/tmp/girl.jpg' #file/tmp/girl查看文件类型;eog /tmp/girl.jpg打开

html = request.urlopen(url)
with open(fname,'wb') as fobj:
    while 1:
        data = html.read(4096)
        if not data:
            break
        fobj.write(data)