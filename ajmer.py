import subprocess
import os
from subprocess import call
import sys,termios
print "The places you wanna visit in Ajmer"
print "> Anasagar Lake"
print "> Nareli Jain Temple"
print "> Ajmer Sharif Dargah"
print "> Lake Foy Sagar"
count = 0
show=raw_input("Please type the places you want to see before you go \n")
while 1:
	if show == 'Anasagar Lake' or show == 'anasagar lake':
		call(['bash','al.sh'])
		count =1
		break
	elif show == 'Nareli Jain Temple' or show == 'nareli jain temple':
		call(['bash','njt.sh'])
		count = 1
		break
	elif show == 'Ajmer Sharif Dargah' or show == 'ajmer sharif dargah':
		call(['bash','aj.sh'])
	   	count = 1
		break
	elif show == 'Lake Foy Sagar' or show == 'lake foy sagar':
		call(['bash','lfs.sh'])
		count = 1
		break
	else:
		print "***Please check the spelling and case***"
		count = 1
		break
while(count=count-1)	
	print "Don't wait, go and EXPLORE"
	os.system("python ajmer.py")	

