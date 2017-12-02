import subprocess
import os
from subprocess import call
import sys, termios
print "The places you want to visit in Jodhpur"
print "> Jaswant Thanda"
print "> Mehrangarh "
print "> Ranisar Padamsar"
print "> Khejarla"
print "> Phoolmahal"
print "> Umaidbhawan"
count = 0
show= raw_input("Please type the places you want to see in Jodhpur\n")
while 1:
	if show == 'Jaswant Thanda' or show == 'jaswant thanda':
		call(['bash','jt.sh'])
		print "Don't wait, go and explore"
		count=1
		break
	elif show == 'Jaswant Thanda' or show == 'jaswant thanda':
		call(['bash','mg.sh'])
		print "Don't wait, go and explore"
		count=1
		break
	elif show == 'Mehrangarh' or show == 'mehrangarh':
		call(['bash','mg.sh'])
		print "Don't wait, go explore"
		count=1
		break
	elif show ==  'Ranisar Padmasar' or show == 'ranisar padmasar':
		call(['bash','rp.sh'])
		print "Don't wait, go explore"
		count=1
		break
	elif show == 'Khejarla' or show == 'khejarla':
		call(['bash','kj.sh'])
		print "Don't wait, go explore"
		count=1
		break
	elif show == 'Phoolmahal' or show == 'phoolmahal':
		call(['bash','pm.sh'])
		print "Don't wait, go explore"
		count=1
		break
	elif show == 'UmaidBhawan' or show == 'umaidbhawan':
		call(['bash','ub.sh'])
		print "Don't wait, go explore"
		count=1
		break
	else:
		print "***please check the spelling and case***"
		count=1
		break
os.system("python jodhpur.py")

