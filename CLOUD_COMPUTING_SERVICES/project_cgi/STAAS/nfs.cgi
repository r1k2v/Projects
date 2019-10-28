#!/usr/bin/python

import os,commands,cgi,cgitb
cgitb.enable()
print "content-type:text/html"
print


form=cgi.FieldStorage()
b=form.getvalue('x')
c=form.getvalue('y')
commands.getstatusoutput("sudo lvcreate  --name  " +b+ " --size " +c+ "M  hdvg")
commands.getstatusoutput("sudo mkdir /media/{0}".format(b))
commands.getstatusoutput("sudo mkfs.ext4 /dev/hdvg/{0}".format(b))
commands.getstatusoutput("sudo mount /dev/hdvg/{0} /media/{0}".format(b))
commands.getstatusoutput("sudo chmod 777  /etc/exports")
commands.getstatusoutput("echo '/media/"+b+ " *(rw,no_root_squash)'>>/etc/exports")
commands.getstatusoutput("exportfs -r")
commands.getstatusoutput("systemctl restart nfs-server")
commands.getstatusoutput("systemctl status nfs-server")
commands.getstatusoutput("systemctl restart nfs-server")
w=commands.getstatusoutput("systemctl status nfs-server")
if w[0]==0:
	commands.getstatusoutput("sudo touch /var/www/html/{}.py".format(b))
	commands.getstatusoutput("sudo chmod 777 /var/www/html/{}.py".format(b))
	f=open("/var/www/html/{}.py".format(b),"w")
	f.write("#!/usr/bin/python\n")
	f.write("import commands,os\n")
	f.write("commands.getstatusoutput('iptables -F')\n")
	f.write("commands.getstatusoutput('setenforce 0')\n")
	f.write("commands.getstatusoutput('mkdir  /media/{}')\n".format(b))
	f.write("commands.getstatusoutput('mount -t nfs 192.168.122.1:/media/{0} /media/{0}')\n".format(b))
	f.close()
	commands.getstatusoutput("sudo tar -cvf /var/www/html/{0}.tar /var/www/html/{0}.py".format(b))
	commands.getstatusoutput("sudo chmod 777 /var/www/html/{0}.tar".format(b))
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/{}.tar\">\n".format(b)  
	commands.getstatusoutput("systemctl restart nfs-server")
	commands.getstatusoutput("systemctl status nfs-server")  
	commands.getstatusoutput("exportfs")     
else:
	print "please give another name"
	
        



#a=raw_input("enter name of mounted folder")
#os.system("/etc/exports","w")
#os.system("file.write("/media/"+a" *(rw,no_root_squash)")")
#os.system("file.close")


