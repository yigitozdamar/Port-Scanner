#!/bin/bash

#(echo > /dev/tcp/192.168.171.135/22) > /dev/null 2>&1 && echo "22 is open" || echo "22 is closed"

fileName="/home/kali/BAA/hostnames.txt" # you must change filepath
while IFS= read -r hostname
do
	echo "----------------------------------"
	echo "Port Scan Starting for $hostname"
	for port in {1..300} # you can change port numbers
	do
		(echo > /dev/tcp/$hostname/$port) > /dev/null 2>&1 && echo "$hostname: $port is open" 
	done
	echo "Port Scan Finished for $hostname"
	echo "----------------------------------"
done < $fileName