#!/usr/bin/python

import os,commands,cgi,cgitb
cgitb.enable()
print "content-type:text/html"
print


form=cgi.FieldStorage()
b=form.getvalue('x')
a=form.getvalue('y')

commands.getstatusoutput("sudo lvextend --size +"+b+"M  /dev/hdvg/"+a)
commands.getstatusoutput("sudo e2fsck -f /dev/hdvg/"+a)
commands.getstatusoutput("sudo resize2fs /dev/hdvg/"+a)

commands.getstatusoutput("sudo df -hT")

