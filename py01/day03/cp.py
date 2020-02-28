#!/usr/local/bin/python3
#将/bin/ls 拷贝到/tmp目录下,不修改原始文件
src_fname='/bin/ls'
dst_fname='/tmp/list'
src_fobj=open(src_fname,'rb')
dst_fobj=open(dst_fname,'wb')

while 1:
    data=src_fobj.read(4096) #从源文件中一次最多读4096
    #if data==b'': data为空
    #if len(data)==0: data长度为0
    if not data:
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()

#验证md5sum /bin/ls /tmp/list
