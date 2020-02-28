#!/usr/local/bin/python3
import os
import requests
import wget
import hashlib
import tarfile


def has_new_ver(ver_fname, ver_url):
    if not os.path.isfile(ver_fname):
        return True

    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    r = requests.get(ver_url)
    if local_ver != r.text:
        return True
    else:
        return False


def file_ok(md5_url, app_fname):
    m = hashlib.md5()
    with open(app_fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    r = requests.get(md5_url)
    if m.hexdigest() == r.text.strip():
        return True
    else:
        return False


def deploy(app_fname, deploy_dir, dest):
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    app_dir = os.path.basename(app_fname)
    app_dir = app_dir.replace('.tar.gz', '')
    app_dir = os.path.join(deploy_dir, app_dir)

    if os.path.exists(dest):
        os.remove(dest)

    os.symlink(app_dir, dest)


if __name__ == '__main__':
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.137.3:8008/deploy/live_ver'
    if not has_new_ver(ver_fname, ver_url):
        print('Not find new verish')
        exit(1)

    down_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = 'http://192.168.137.3:8008/deploy/pkgs/myweb-%s.tar.gz' % r.text
    wget.download(app_url, down_dir)

    md5_url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(down_dir, app_fname)
    if not file_ok(md5_url, app_fname):
        print('Bad File')
        os.remove(app_fname)
        exit(2)

    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd1909'
    deploy(app_fname, deploy_dir, dest)

    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)

    print('OK')
