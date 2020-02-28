#!/usr/local/bin/python3
# PEP:Python Enhanced Proposat #代码书写规范#pycharm的快捷键ctrl+alt+l

from time import strftime
import hashlib
import sys
import os
import tarfile
import pickle


def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while 1:  # 非文本文件,分批读取
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def full_backup(src, dst, md5file):
    '完全备份'

    # 拼接出备份文件的绝对路径
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 打包压缩
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算md5值

    # >>> a = {}
    # >>> a['name'] = 'tom'
    # >>> a
    # {'name': 'tom'}

    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            k = os.path.join(path, file)
            md5dict[k] = check_md5(k)

    # 将md5字典保存到文件中
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


def incr_backup(src, dst, md5file):
    '增量备份'

    # 拼接出备份文件的绝对路径
    fname = '%s_incr_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 计算每个文件的md5值,保存到字典中
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            k = os.path.join(path, file)
            md5dict[k] = check_md5(k)

    # 取出前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 字典的key是文件名,key在今天有,昨天没有,就是新增文件,文件的md5值不一样,就是改动文件
    # 新增的文件和改动的文件需要备份
    tar = tarfile.open(fname, 'w:gz')
    for k in md5dict:
        if old_md5.get(k) != md5dict[k]:
            tar.add(src)
    tar.close()

    # 更新md5文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


if __name__ == '__main__':

    # mkdir /tmp/demo
    # cp -r /etc/security/ /tmp/demo
    # mkdir /tmp/demo/backup
    # tar tvzf 包 #只打开,不解压

    src = '/tmp/demo/security'  # 源,目标地址
    dst = '/tmp/demo/backup'  # 备份地址
    md5file = '/tmp/demo/backup/md5.data'  # hash值备份文件

    # >>> time.strftime('%a')
    # 'Tue'
    if strftime('%a') == 'Mon':  # 周一完全备份
        full_backup(src, dst, md5file)
    else:  # 其余时间增量备份
        incr_backup(src, dst, md5file)
