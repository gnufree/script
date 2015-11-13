#!/usr/bin/env python
# coding:utf-8
import urllib
import re
import sys
ip = sys.argv[1]
uip = urllib.urlopen('http://www.ip.cn/index.php?ip=%s'%ip)
fip = uip.read()
rip = re.compile(r';来自：(.+)</p><p>GeoIP:')
result = rip.findall(fip)
#print result
print "%s \t %s" %(ip,result[0])
#print fip
