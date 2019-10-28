#!/usr/bin/python

import os,commands,cgi,cgitb
cgitb.enable()

print "content-type:text/html"
print


x=cgi.FieldStorage()
c=x.getvalue('p')
	
d=x.getvalue('r')

w=commands.getstatusoutput(" sudo lvcreate  --name  " +d+ " --size " +c+ "M  hdvg")

while w[0] != 0:
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/iscsi.html\">\n"
        x=cgi.FieldStorage()
	c=x.getvalue('p')
	
	d=x.getvalue('r')
	
	w=commands.getstatusoutput(" sudo lvcreate  --name  " +d+ " --size " +c+ "M  hdvg")
        
else:
	commands.getstatusoutput("sudo touch /{}.conf".format(d))
	
	commands.getstatusoutput("sudo chmod 777 /{}.conf".format(d))
	f=open("/{}.conf".format(d),"a")
	f.write("<target {0}>\n    backing-store   /dev/hdvg/{0} \n</target> ".format(d))
	f.close()
	p=commands.getstatusoutput("sudo mv  /{}.conf  /etc/tgt/conf.d/".format(d))

		
	commands.getstatusoutput("sudo systemctl restart tgtd")
		
		
	commands.getstatusoutput("sudo systemctl status tgtd")
	m=commands.getstatusoutput(" sudo tgt-admin -show")

	if m[0] != 0  :
		print " not ok"
	else:
		commands.getstatusoutput("sudo touch /block/{}.py".format(d))
	
		commands.getstatusoutput("sudo chmod 777 /block/{}.py".format(d))
		f=open("/block/{}.py".format(d),"a")
		f.write("#!/usr/bin/python\nimport commands,os,time\ncommands.getstatusoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.122.1  --discover')\ncommands.getstatusoutput('iscsiadm --mode node --targetname  {} --portal 192.168.122.1:3260 --login')\nos.system('fdisk -l')\n".format(d))
		f.write("raw_input()")
		f.close()
		commands.getstatusoutput("sudo tar -cvf /var/www/html/{0}.tar /block/{0}.py".format(d))
		commands.getstatusoutput("sudo chmod 777 /var/www/html/{0}.tar ")
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/{}.tar\">\n".format(d)

	
