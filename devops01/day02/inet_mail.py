#!/usr/local/bin/python3
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass


def send_email(body, sender, receivers, subject, server, passwd):
    # 准备邮件
    # plain表示纯文本,相对于富文本
    msg = MIMEText(body, 'plain', 'utf8')
    # 添加头部信息
    msg['From'] = Header(sender, 'utf8')  # 发件人
    msg['To'] = Header(receivers[0], 'utf8')  # 收件人
    msg['Subject'] = Header(subject, 'utf8')  # 主题

    # 发送邮件
    smtp = smtplib.SMTP()  # 使用本机发送邮件
    smtp.connect(server)
    # smtp.starttls() # 如果服务器要求安全连接,则打开注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, msg.as_bytes())


if __name__ == '__main__':
    body = '测试\n'
    sender = '1458351621@qq.com'
    receivers = ['1458351621@qq.com', '1458351621@qq.com']
    subject = 'py mail'
    server = 'smtp.qq.com'
    passwd = getpass.getpass()
    send_email(body, sender, receivers, subject, server, passwd)
