#!/usr/bin/python2

import cgi,commands
print "content-type:text/html"
print

x=cgi.FieldStorage()

name=x.getvalue('c')
passwd=x.getvalue('d')
email=x.getvalue('b')
names=x.getvalue('a')
cno=x.getvalue('e')




x=commands.getstatusoutput("sudo locate -c /home/{}".format(name))
if x[0] != 0:
	
	a=commands.getstatusoutput("sudo useradd {}".format(name))


	d=commands.getstatusoutput("echo {1}|sudo passwd {0}  --stdin".format(name,passwd))

	
	f=open("/users","a")
	f.write("{0}:{1}:{2}:{3}\n".format(name,passwd,email,cno))
	f.close()
	
	print ("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/first.html\">\n")
	
else:
	print ("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/index.html\">\n")
	
 
