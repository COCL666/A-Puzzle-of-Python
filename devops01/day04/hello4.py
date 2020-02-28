#!/usr/local/bin/python3

# CI/CD:持续集成/持续交互(部署)

# dev(程序员)--推送-->git(git服务器)
# jenkins(jenkins)--拉取-->git
# app1(app server)--下载-->jenkins
# app2(app server)--下载-->jenkins
# app3(app server)--下载-->jenkins

# 程序：
# 解释执行：shell / python / php # 速度慢,但易编写,方便开发
# 编译执行：c / go # gcc -c 输入文件 -o 输出文件 # 速度快,难实现功能



# git
# 安装: yum -y install git

# 配置
# git config --global user.name 'zhongli'
# git config --global user.email 'zhongli_cocl666@163.com'
# git config --global core.editer vim # 指定默认编辑器

# [root@zl2 ~]# git config --list
# core.editer=vim
# user.name=zhongli
# user.email=zhongli_cocl666@163.com

# [root@zl2 ~]# cat ~/.gitconfig
# [core]
# 	editer = vim
# [user]
# 	name = zhongli
# 	email = zhongli_cocl666@163.com

# git的工作区域
# 工作区:软件项目目录
# 暂存区:.git/index(索引),是工作区与版本库间的缓冲地带
# 版本库:工作区下的git目录
# 工作区--git add-->暂存区--git commit-->版本库

# 创建版本库方法一(有代码前)
# [root@zl2 ~]# git init myproject
# 初始化空的 Git 版本库于 /root/myproject/.git/
# [root@zl2 ~]# ls -A myproject/
# .git

# 创建版本库方法二(已经有代码了)
# [root@zl2 ~]# mkdir myweb
# [root@zl2 ~]# cd myweb/
# [root@zl2 myweb]# echo '<h1>my web site</h1>' > index.html
# [root@zl2 myweb]# git init
# 初始化空的 Git 版本库于 /root/myweb/.git/
# [root@zl2 myweb]# ls -A
# .git  index.html

# 初始化版本库,不会将文件存入版本库
# [root@zl2 myweb]# cp /etc/passwd .
# [root@zl2 myweb]# git status
# [root@zl2 myweb]# git status -s
# ?? index.html     # ??表示状态未知
# ?? passwd
# [root@zl2 myweb]# git add index.html
# [root@zl2 myweb]# git status -s
# A  index.html     # 表示文件已添加到暂存区
# ?? passwd
# [root@zl2 myweb]# git add .   #将当前目录所有内容加入到暂存区
# [root@zl2 myweb]# git status -s
# A  index.html
# A  passwd
# 将文件从暂存区撤出
# [root@zl2 myweb]# git rm --cached passwd
# rm 'passwd'
# [root@zl2 myweb]# git status -s
# A  index.html
# ?? passwd

# 通过.gitignore忽略不想加入到版本库的文件
# [root@zl2 myweb]# vim .gitignore
# passwd
# *.swp
# .gitignore
# root@zl2 myweb]# git status -s
# A  index.html

# 提交文件到版本库
# [root@localhost myweb]# git commit  # 跳出vim，不写入任何内容，直接退出,不会提交
# [root@localhost myweb]# git status -s  # 文件仍然在暂存区
# A  index.html
# [root@localhost myweb]# git commit -m "first commit"  # 直接提交
# [root@localhost myweb]# git status -s
# [root@localhost myweb]# git status
# # 位于分支 master
# 无文件要提交，干净的工作区

# 查看版本库中的文件
# [root@zl2 myweb]# git ls-files
# index.html
# 查看工作区中的文件
# [root@zl2 myweb]# ls
# index.html  passwd

# 删除文件
# [root@zl2 myweb]# git rm index.html
# rm 'index.html'
# [root@zl2 myweb]# ls
# passwd
# [root@zl2 myweb]# git ls-files
#
# [root@zl2 myweb]# git status -s
# D  index.html
# [root@zl2 myweb]# git status
# # 位于分支 master
# # 要提交的变更：
# #   （使用 "git reset HEAD <file>..." 撤出暂存区）
# #
# #	删除：      index.html
# #
# [root@zl2 myweb]# git reset HEAD index.html
# 重置后撤出暂存区的变更：
# D	index.html
# [root@zl2 myweb]# git status -s
#  D index.html
# [root@zl2 myweb]# git status
# # 位于分支 master
# # 尚未暂存以备提交的变更：
# #   （使用 "git add/rm <file>..." 更新要提交的内容）
# #   （使用 "git checkout -- <file>..." 丢弃工作区的改动）
# #
# #	删除：      index.html
# #
# 修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）

# [root@zl2 myweb]# git checkout -- index.html
# [root@zl2 myweb]# ls
# index.html  passwd
# [root@zl2 myweb]# git ls-files
# index.html
# [root@zl2 myweb]# git status
# # 位于分支 master
# 无文件要提交，干净的工作区

# 恢复误删除的文件
# [root@localhost nsd2019]# pwd
# /tmp/nsd2019
# [root@localhost nsd2019]# du -sh .
# 232M    .
# [root@localhost nsd2019]# du -sh .git
# 83M .git
# [root@localhost nsd2019]# rm -rf *
# [root@localhost nsd2019]# ls -A
# .git  .gitignore
# [root@localhost nsd2019]# du -sh
# 83M .
# [root@localhost nsd2019]# git status | more
# # 位于分支 master
# # 尚未暂存以备提交的变更：
# #   （使用 "git add/rm <file>..." 更新要提交的内容）
# #   （使用 "git checkout -- <file>..." 丢弃工作区的改动）
# #
# #   删除：      README.md
# [root@localhost nsd2019]# git checkout -- *
# [root@localhost nsd2019]# ls
# [root@localhost nsd2019]# du -sh .
# 232M    .

# 删除版本库中的文件
# [root@localhost myweb]# git ls-files
# index.html
# [root@localhost myweb]# ls
# index.html  passwd
# [root@localhost myweb]# git rm index.html
# rm 'index.html'
# [root@localhost myweb]# git commit -m "delete index.html"
# [root@localhost myweb]# ls
# passwd
# [root@localhost myweb]# git status
# # 位于分支 master
# 无文件要提交，干净的工作区
# [root@localhost myweb]# git ls-files   # 版本库中也已经没有index.html了

# 查看日志
# [root@localhost myweb]# git log
# commit e6ea007564e9b113e62741247c3c595dd34d8202
# Author: MrZhangzhg <zhangzg@tedu.cn>
# Date:   Tue Feb 25 11:29:13 2020 +0800
#
#     delete index.html
#
# commit 2293660c978ce857b0a6d9d29fae59cf7d4fa9a7
# Author: MrZhangzhg <zhangzg@tedu.cn>
# Date:   Tue Feb 25 10:41:30 2020 +0800
#
#     first commit

# 删除文件并提交后如何恢复
# reset到以前的未删除的状态
# [root@zl2 myweb]# ls
# passwd
# [root@zl2 myweb]# git log --oneline
# 5deb865 delete index.html
# 9c09c8a first commit
# [root@zl2 myweb]# git reset --hard 9c09c8a
# HEAD 现在位于 9c09c8a first commit
# [root@zl2 myweb]# ls
# index.html  passwd
# [root@zl2 myweb]# git ls-files
# index.html

# checkout返回最新状态
# 返回到master分支最新状态
# [root@localhost myweb]# ls   # 工作区中出现index.html
# index.html  passwd
# [root@localhost myweb]# git checkout master
# 之前的 HEAD 位置是 9c09c8a first commit
# 切换到分支 'master'
# [root@localhost myweb]# ls   # 工作区中没有index.html
# passwd

# 改名
# [root@localhost myweb]# cp /etc/hosts .
# [root@localhost myweb]# git add .
# [root@localhost myweb]# git commit -m "add hosts"
# [root@localhost myweb]# git mv hosts zhuji
# [root@localhost myweb]# git status -s
# R  hosts -> zhuji    # rename
# [root@localhost myweb]# git commit -m "mv hosts zhuji"
# [root@localhost myweb]# git ls-files
# zhuji
# [root@localhost myweb]# ls
# passwd  zhuji

# 分支管理
# git中有一个默认的分支叫master
# [root@localhost myweb]# git branch
# * master
# 当需要把某一个需求交给某人处理时,就可以创建一个新的分支,代码在分支中完成,当分支功能完成后,可以再汇入主干
# 创建分支b1
# [root@localhost myweb]# git branch b1
# [root@localhost myweb]# git branch
#   b1
# * master   # 有*号的，表示当所处分支
# 在master分支上提交代码
# [root@localhost myweb]# cp /etc/shadow .
# [root@localhost myweb]# git add .
# [root@localhost myweb]# git commit -m "add shadow"
# [root@localhost myweb]# ls
# passwd  shadow  zhuji
# 在b1分支提交代码
# [root@localhost myweb]# git checkout b1   # 切换分支
# [root@localhost myweb]# git branch
# * b1
#   master
# [root@localhost myweb]# ls   # 没有shadow文件
# passwd  zhuji
# [root@localhost myweb]# cp /etc/issue .
# [root@localhost myweb]# git add .
# [root@localhost myweb]# git commit -m "add issue"
# [root@localhost myweb]# ls
# issue  passwd  zhuji
# 将b1分支汇入到主干master
# [root@localhost myweb]# git checkout master
# [root@localhost myweb]# ls
# passwd  shadow  zhuji
# [root@localhost myweb]# git merge b1 -m "Merge branch b1"
# [root@localhost myweb]# ls
# issue  passwd  shadow  zhuji
# [root@localhost myweb]# git branch -d b1   # 删除不需要的分支
# [root@localhost myweb]# git branch
# * master

# 标记
# 可以为某一次commit打一个标记,如作为版本号
# [root@zl2 myweb]# git tag
# [root@zl2 myweb]# git tag 1.0
# [root@zl2 myweb]# git tag
# 1.0
# [root@zl2 myweb]# cp /etc/motd .
# [root@zl2 myweb]# git add .
# [root@zl2 myweb]# git commit -m "add motd"
# [master 8a2996e] add motd
#  1 file changed, 0 insertions(+), 0 deletions(-)
#  create mode 100644 motd
# [root@zl2 myweb]# git tag 2.0
# [root@zl2 myweb]# git tag
# 1.0
# 2.0

# gitlab
# git服务器有很多种类型,如github/gitlab/gogs/gitee等
# 不要太相信别人提供的服务,要给自己备份
# 生产环境不要rm -rf ,要mv到回收站
# 安装docker并启动
# 导入gitlab镜像
# 修改主机ssh端口为2022
# [root@zl2 ~]# vim /etc/ssh/sshd_config
# Port 2022
# [root@zl2 ~]# systemctl restart sshd
# [root@zl2 ~]# ssh -p2022 192.168.137.3
# 启动容器
# docker run -d -h gitlab --name gitlab -p 443:443 -p 80:80 -p 22:22 --restart always -v /srv/gitlab/config:/etc/gitlab -v /srv/gitlab/logs:/var/log/gitlab -v /srv/gitlab/data:/var/opt/gitlab gitlab_zh:latest
# 查看状态,当状态成为healthy时,才完全可用
# [root@zl2 ~]# docker ps -a
#

# gitlab中的重要概念
# 用户:使用gitlab的人
# 群组:可以对应开发团队
# 项目:对应开发的项目,可以为个人创建项目,也可以为团队创建项目
# 创建用户:zl.创建用户时,不能设置密码,但是可以在创建后编辑它,这时更改密码.
# 创建名为devops的组并将用户加入到组中.群组类型选:公开.新用户加入到组中的身份是:主程序员.
# 创建名为myweb的项目,项目为devops组创建,可见等级为公开.因为项目是为devops组>创建的,所以devops组的成员,都可以访问该项目.如果需要添加额外成员,可以点击左边栏的设置->成员进行添加.

# 上传代码
# 切换成创建的普通用户.普通用户第一次登陆时,需要改密码,可以改成与之前一样的密码.

# 在程序员的机器上将myweb项目推送到gitlab服务器
# [root@zl2 nsd2019]# echo '192.168.137.3 gitlab' >> /etc/hosts
# 添加仓库,将仓库与url关联
# [root@localhost myweb]# git remote add origin http://gitlab/devops/myweb.git
# 推送代码到gitlab服务器，需要填写用户名,密码.注意,这不会推送tag.
#[root@zl2 myweb]# git push -u origin --all
# Username for 'http://gitlab': cocl
# Password for 'http://cocl@gitlab':
# Counting objects: 6, done.
# Delta compression using up to 4 threads.
# Compressing objects: 100% (3/3), done.
# Writing objects: 100% (6/6), 469 bytes | 0 bytes/s, done.
# Total 6 (delta 0), reused 0 (delta 0)
# To http://gitlab/devops/myweb.git
#  * [new branch]      master -> master
# 分支 master 设置为跟踪来自 origin 的远程分支 master.

# 在gitlab上的仓库页面刷新，可以看到推送上来的代码，但是“标签”显示为0。另外工作区中的passwd因为写入到了.gitigore中，它是被忽略的。上传是将版本库上传，不是工作区。
# 推送标签到gitlab
# [root@localhost myweb]# git push -u origin --tags
# Username for 'http://gitlab': cocl
# Password for 'http://cocl@gitlab':
# Total 0 (delta 0), reused 0 (delta 0)
# To http://gitlab/devops/myweb.git
#  * [new tag]         1.0 -> 1.0
#  * [new tag]         2.0 -> 2.0
# 在gitlab上刷新,可以看到标签.

# 删仓库 git remote remove 库名
# 查看仓库 git remote show

# 使用ssh免密上传代码
# 在程序员的主机上创建密钥对
# [root@zl2 myweb]# ssh-keygen -C "zhongli_cocl666@163.com"
# [root@zl2 myweb]# cat ~/.ssh/id_rsa.pub
# ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDl/jg2Z9P1W55QmRVJ+vzB7QuB78HXlm4CbiFALrTVb+m522Z8Kk9wfnNKw7JX9V7tDcCT5I7tLAylGi5jskSSQfBDpL+6BmCrMBcKGS7h8G+4JjpKJ3xI9U/I5SESGEUEEhNjma1b/PiU3ixAlHGJCy+B4GTaBo1SPr3vvnu1s0hv07hABjmqnCk9SkXYHM/0O1LMSG7zZ1X8ldq26nHbsjwpRQ/R2noTDKCQkf6+0JpEpxk5LfWn+vj5SD9Lbmo0LP2WE29FSGeeCkYMT/K3gF8TsyfEMCv7SW4JYYWH6hhb1cuydJEExZvOyeV9fw9ca6f3nLg6pCZp3wItWpRcCnLgnqz6x/goSj66Ts04UDoGQskxPoA8WHeGf42mhHViwv5K6eZ3fCHaQigP1Z7G42aF2v+6zY2KayEDCNpdDm77kq+1R+pL87kPnAMoxNjJFW6gZHVH5EsmuXcrQUWlc2kQ7ucCT6WHN8E1lWYe/MfMYXUT3UDqFUpvzaQkwwIE+5wdCbD8KN1DK0jrN4Oez8416FNTlaoUL2ofyJjGG7VwMX4nbfngQMaS2HUESf7wN35gvw+9KdWQr2pyOFYkDo6Fs88l1Xl9m10UYS2m5T+x7hSBiohK3Eqarr6MyitZaPyHGhBjDtef2uBkTdCjJ8zKUNtXKpnXO9nEZlf3pQ== zhongli_cocl666@163.com
# 复制公钥内容
# 在gitlab页面的右上角点击用户图标->设置->窗口左边栏ssh密钥(个人资料).将复制的公钥信息粘贴到密钥文本框中.
#
# 修改git仓库上传代码的方式.
#
# 删后
# [root@zl2 myweb]# git remote remove origin
# [root@zl2 myweb]# cat .git/config
# [core]
# 	repositoryformatversion = 0
# 	filemode = true
# 	bare = false
# 	logallrefupdates = true
# [branch "master"]

# 增加,使用ssh免密
# [root@zl2 myweb]# git remote add origin git@gitlab:devops/myweb.git
# [root@zl2 myweb]# cat .git/config
# [core]
# 	repositoryformatversion = 0
# 	filemode = true
# 	bare = false
# 	logallrefupdates = true
# [branch "master"]
# [remote "origin"]
# 	url = git@gitlab:devops/myweb.git
# 	fetch = +refs/heads/*:refs/remotes/origin/*

# 上传测试
# [root@localhost myweb]# vim README.md
# # 我的测试项目
# ```python
# >>> print("Hello World!")
# ```
# - 本项目仅用于演示使用
# - 可以通过http下载
# - 也可以通过ssh上传下载
# [root@localhost myweb]# git add .
# [root@localhost myweb]# git commit -m "add readme.md"
# [root@localhost myweb]# git push
