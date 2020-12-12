#!/usr/bin/python3
import pyfiglet 
import sys 
import socket 
from datetime import datetime 

ascii_banner = pyfiglet.figlet_format("YIGIT's Scanner") 
print(ascii_banner) 

print("-" * 50)
print("Scanning started at:" + str(datetime.now())) 
print("-" * 50) 

try:
	with open("filename") as fp: # filename path: file that contains ip adresses ex: /home/kali/hostnames.txt
	    lines = fp.readlines()
	    for ip in lines:
	    	target = socket.gethostbyname(ip.strip())
	    	print("-" * 20)
	    	print("Scanning IP: ", target)
	     # It will scan ports between 1 to 65,535 you can change it
	    	for port in range(1,65535): 
	        	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	        	socket.setdefaulttimeout(1) 
	          
	        # returns an error indicator 
	        	result = s.connect_ex((target,port)) 
	        	if result == 0:
	        		print(target, ":" ,"Port ", port, "is open")
	        	s.close() 
          
except KeyboardInterrupt: 
        print("\n Exitting Program !!!!") 
        sys.exit() 
except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit() 
except socket.error: 
        print("\ Server not responding !!!!") 
        sys.exit()

# Add Banner 
