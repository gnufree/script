#!/usr/bin/python
# coding: utf-8

import smtplib
from email.mime.text import MIMEText    #导入MIMEText类

HOST = "smtp.126.com"
SUBJECT = u"官网流量数据报表"
TO = "mymail@qq.com"
FROM = "mymail@126.com"
msg = MIMEText( # 创建一个MIMEText对象，分别指定HTML内容、类型(文本或html)、字符编码)
    """
    <table width="800" border="0" cellspacing="0" collpadding="4">
    <tr>
        <td bgcolor="#CECFAD" height="20" style="font-size:14px">*官网数据<a
        href="monitor.domain.com">更多>></a></td>
    </tr>
    <tr>
        <td bgcolor="#EEEEEE" height="100" style="font-size:13px">
        1)日访问量<br>
        2)状态信息<br>
        &nbsp;&nbsp;500:105 404:2322 503:214<br>
        3)访客浏览器信息<br>
        &nbsp;&nbsp;IE:50% firefox:10% chrome:30% other:10%<br>
        4)页面信息<br>
        &nbsp;&nbsp;/index.php 23232<br>
        &nbsp;&nbsp;/view.php 232<br>
        &nbsp;&nbsp;/login.php 232<br>
        </td>
    </tr>
    <tr>
        <td></td>
    </tr>
    </table>""","html","utf-8")
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['TO'] = TO
try:
    server = smtplib.SMTP()
    server.connect(HOST,"25")
    server.starttls()
    server.login("mymail@126.com","mypasswd")
    server.sendmail(FROM,TO,msg.as_string())
    server.quit()
    print "邮件发送成功！"
except Exception, e:
    print "邮件发送失败: "+str(e)

