#!/usr/bin/python2
import socket

#below method with argument creating a socket called s
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

s.sendto("aaj ki class khtm",("192.168.10.177",9999))



