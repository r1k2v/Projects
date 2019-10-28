#!/usr/bin/python

import os,commands


p=commands.getstatusoutput("virt-install --name galleryOs2 --ram 1024 --vcpu 1 --disk path=/var/lib/libvirt/images/rhel72.qcow2   --graphics vnc,listen=0.0.0.0,port=6002 --noautoconsole --import")
print p
v=commands.getstatusoutput("sudo /root/Desktop/websockify-master/run -D 192.168.122.1:6052 192.168.122.1:6002")

#print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/vnc/index.html?host=192.168.122.1&port=6052\">\n"	
raw_input()
