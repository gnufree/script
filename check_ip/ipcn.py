#!/usr/bin/python
# coding:utf-8

import sys
import os
import re
import urllib

file_object = open("badip.txt")
for line in file_object.readlines():
    l = re.split(r'=',line)
    ip = l[1]
    uip = urllib.urlopen('http://www.ip.cn/index.php?ip=%s'%ip)
    fip = uip.read()
    rip = re.compile(r';来自：(.+)</p><p>GeoIP:')
    result = rip.findall(fip)
    print "%s \t %s" % (ip,result[0])

