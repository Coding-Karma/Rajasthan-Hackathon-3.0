import subprocess
import os
from subprocess import call
import sys, termios
print "The places you want to visit in Udaipur"

print "> Lake pi cola"
print "> Lake palace"
print "> Monsoon"
print "> Udaipur city palace"

count = 0
show= raw_input("Please type the places you want to see in Udaipur\n")
while 1:
	
	if show == 'Lake Pi cola' or show == 'lake pi cola':
		call(['bash','lp.sh'])
		print "Don't wait, go and explore"
		count=1
		break
	elif show == 'Lake Palace' or show == 'lake palace':
		call(['bash','lpl.sh'])
		print "Don't wait, go explore"
		count=1
		break
	elif show ==  'Monsoon' or show == 'monsoon':
		call(['bash','ms.sh'])
		print "Don't wait, go explore"
		count=1
		break
	elif show == 'Udaipur City Palace' or show == 'udaipur city palace':
		call(['bash','ucp.sh'])
		print "Don't wait, go explore"
		count=1
		break
	else:
		print"***please check the spelling and CASE***"
		break
os.system("python udaipur.py")

