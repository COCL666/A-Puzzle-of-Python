#!/usr/local/bin/python3
# 下载一个页面上的所有图片

# 1.找到所有图片的url地址
#
import os
import wget
import re


def get_patt(fname, patt, charset=None):  # 不写为默认utf8
    result = []
    cpatt = re.compile(patt)

    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())

    return result


if __name__ == '__main__':
    # 创建下载目录
    dst = '/tmp/163'
    if not os.path.exists(dst):
        os.mkdir(dst)

    # 下载首页文件
    fname = '/tmp/163/163.html'
    url = 'http://www.163.com'
    if not os.path.exists(fname):
        wget.download(url, fname)

    # 在首页文件中找到所有图片的url
    img_patt = '(http|https)://[\w./-]+\.(jpg|png|jpeg|gif)'
    img_list = get_patt(fname, img_patt, 'gbk')  # 网易首页是gbk编码

    # 下载图片
    for img_url in img_list:
        wget.download(img_url, dst)
