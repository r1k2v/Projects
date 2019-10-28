#!/usr/bin/python

import os,commands,cgi,cgitb,time
import random
cgitb.enable()

print "content-type:text/html"
print

form=cgi.FieldStorage()
p=form.getvalue('a')
r=form.getvalue('b')
s=form.getvalue('c')
t=form.getvalue('d')
u=form.getvalue('e')
server=random.randint(5931,5945)
web=random.randint(5586,5599)
print server
print web
p1=commands.getstatusoutput("sudo qemu-img create -f qcow2 /var/lib/libvirt/images/{0}.qcow2  {1}".format(p,t))

p2=commands.getstatusoutput("sudo virt-install --hvm --name {0} --ram {1} --disk /var/lib/libvirt/images/{0}.qcow2 --vcpu {2} --cdrom /root/Desktop/rhel-server-7.2-x86_64-dvd.iso --os-type linux --noautoconsole --os-variant rhel7 --graphics vnc,listen=0.0.0.0,port={3}".format(p,s,u,server))
p3=commands.getstatusoutput("sudo /root/Desktop/websockify-master/run -D 192.168.122.1:{0} 192.168.122.1:{1}".format(web,server))
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/vnc/index.html?host=192.168.122.1&port={0}\">\n".format(web)
