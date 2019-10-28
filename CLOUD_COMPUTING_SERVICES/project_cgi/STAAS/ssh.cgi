#!/usr/bin/python

import os,commands,cgi,cgitb
cgitb.enable()
print "content-type:text/html"
print


form=cgi.FieldStorage()
b=form.getvalue('x')
c=form.getvalue('y')
commands.getstatusoutput("sudo iptables -F")
commands.getstatusoutput("sudo setenforce 0")
w=commands.getstatusoutput("sudo lvcreate  --name  " +c+ " --size " +b+ "M  hdvg")
if w[0] == 0:
	commands.getstatusoutput("sudo mkdir /media/{0}".format(c))
	commands.getstatusoutput("sudo mkfs.ext4 /dev/hdvg/{0}".format(c))
	v=commands.getstatusoutput("sudo mount /dev/hdvg/{0} /media/{0}".format(c))
	if v[0]==0:
		commands.getstatusoutput("sudo touch /var/www/html/{}.py".format(c))
		commands.getstatusoutput("sudo chmod 777 /var/www/html/{}.py".format(c))
		f=open("/var/www/html/{}.py".format(c),"w")
		f.write("#!/usr/bin/python \n")
		f.write("import os,commands \n")
                f.write('commands.getstatusoutput("mkdir /media/'+c+'")\n')
		f.write('commands.getstatusoutput("sshfs root@192.168.122.1:/media/'+c+'  /media/'+c+'")\n')
		f.write("raw_input()")
		f.close()
		commands.getstatusoutput("sudo tar -cvf /var/www/html/{0}.tar  /var/www/html/{0}.py".format(c))
		commands.getstatusoutput("sudo chmod 777 /var/www/html/{}.tar".format(c))
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/{}.tar\">\n".format(c) 
 
	        
else:
	print "please give another name"
