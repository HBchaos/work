#!/usr/bin/python2
import socket

rec_ip="192.168.10.177"
myport=9999

#below method with argument creating a socket called s
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #onlyforreciever #AF_INITforIPV,#SOCK.DGRAMforUDP

#now connecting ip and port
s.bind((rec_ip,myport))

#buffer size

while 4>2 :
	print s.recvfrom(100)	
	


