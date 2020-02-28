#!/usr/local/bin/python3
import hashlib,sys

def check_md5(fname):

    m = hashlib.md5()

    with open(fname,'rb') as fobj:
        while 1: #非文本文件,分批读取
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

if __name__ == '__main__':
    print(check_md5(sys.argv[1])+'  '+sys.argv[1])