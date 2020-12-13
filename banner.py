#!/usr/bin/python3
import pyfiglet 
import sys 
import socket 
from datetime import datetime
import select 

ascii_banner = pyfiglet.figlet_format("YIGIT's Scanner") 
print(ascii_banner) 

print("-" * 50)
print("Scanning started at:" + str(datetime.now())) 
print("-" * 50) 

try:
	with open("/home/kali/BAA/hostnames.txt") as fp: # You must change the filepath
	    lines = fp.readlines()
	    for ip in lines:
	    	target = socket.gethostbyname(ip.strip())
	    	print("-" * 20)
	    	print("Scanning IP: ", target)
	     # This will scan ports between 1 to 65,535 
	    	for port in range(1,100): 
	        	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        	socket.setdefaulttimeout(1)
	        	
	        # Returns an error indicator 
	        	result = s.connect_ex((target,port)) 
	        	if result == 0:
	        		service = socket.getservbyport(port)
	        		ready = select.select([s],[],[],1)
	        		if ready[0]:
	        			print(target, ":" ,"Port ", port, " is open","-->",service,":", s.recv(1024).strip())
	        	else:
	        		pass	        		
	        	s.close() 
          
except KeyboardInterrupt: 
        print("\n Exitting Program !!!!") 
        sys.exit() 
except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit() 
except socket.error: 
        print(target, "\ Server not responding !!!!") 
        sys.exit()


