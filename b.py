#!/usr/bin/python
import time
import whoami
import uname
import nmap

print "press 1 to check time:"
print "press 2 to check user:"
print "press 3 to check kernel"
print "press 4 to check network"


ch=raw_input()
if ch=='1':
 print time.ctime() 

if ch=='2':
 print whoami() 

if ch=='1':
 print uname() 

if ch=='1':
 print nmap() 
 





else :
 print "nope!" 
