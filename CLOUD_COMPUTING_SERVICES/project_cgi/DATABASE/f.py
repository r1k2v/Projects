#!/usr/bin/python2

import cgi,commands
 
print "content-type:text/html"
print

form = cgi.FieldStorage()
name = form.getvalue('a')
passwd = form.getvalue('b')





vr=commands.getstatusoutput("sudo cat /users|grep {}".format(name))

if vr[0]==0:
	f=open('/users','r')
	t=f.readlines()
	f.close()
	
	for i in t :
		
		fg = i.split(':')[0] 
		
		if fg == name:
			gg=i.split(':')[1]
			
			if gg==passwd:
				
				print  ("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/first.html\">\n")
      			else:
				
				print  ("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/index.html\">\n")
		
