#!/usr/bin/python
# coding:utf-8
import smtplib
import string

HOST = "smtp.126.com" # 定义smtp主机
SUBJECT = "Test email from Python"  # 定义邮件主题
TO = "mymail@qq.com"  # 定义邮件收件人
FROM = "mymail@126.com"  # 定义邮件发件人
text = "Python rules them all!" # 邮件内容
BODY = string.join((    # 组装sendmail方法的邮件主体内容，各段以"\r\n" 进行分割
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
    ),"\r\n")
server = smtplib.SMTP()   # 创建一个SMTP()对象
server.connect(HOST,"25") # 通过connect方法连接smtp主机
server.starttls()         # 启动安全传输模式
server.login("mymail@126.com","mypasswd")  # 邮箱账号登陆效验
server.sendmail(FROM,[TO],BODY)   # 邮件发送
server.quit()

