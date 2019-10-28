#!/usr/bin/python

import cgi,commands,cgitb
cgitb.enable()

print "content-type:text/html"
print ""

c=cgi.FieldStorage()
m=c.getvalue('x')
n=c.getvalue('y')
o=c.getvalue('w')



commands.getstatusoutput("sudo touch /var/www/html/{}.py".format(m))
commands.getstatusoutput("sudo chmod 777 /var/www/html/{}.py".format(m))
f=open("/var/www/html/{}.py".format(m),"w")
f.write("#!/usr/bin/python\nimport commands,time\ncommands.getstatusoutput('sshpass -p {} ssh -X -l {} 192.168.122.1 {}')\nraw_input()".format(n,m,o))
f.close()
commands.getstatusoutput("sudo tar -cvf /var/www/html/{0}.tar /var/www/html/{0}.py".format(m))
commands.getstatusoutput("chmod 777 /var/www/html/{}.tar".format(m))
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/{}.tar\">\n".format(m)


		
