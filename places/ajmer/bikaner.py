import subprocess
import os
from subprocess import call
import sys,termios
print "The places you wanna visit in bikaner"
print "> Deshnok karni mata temple"
print "> Lalgarh Place and Museum"
print "> Jain Temple Bhandasar"
print "> Rampuria Haveli"
print "> Junagarh Fort"
print "> Shir Lakshminath Temple"
count = 0
show=raw_input("Please type the places you want to see before you go \n")
while 1:
	if show == 'Deshnok Karni Mata Temple' or show == 'deshnok karni mata temple':
		call(['bash','dkmt.sh'])
		print "Don't wait, go and EXPLORE" 
		count =1
		break
	elif show == 'Lalgarh Palace and Museum' or show == 'lalgarh palace and museum':
		call(['bash','lpam.sh'])
		print "Don't wait, go and EXPLORE" 
		count = 1
		break
	elif show == 'Jain Temple Bhandasar' or show == 'jain temple bhandasar':
		call(['bash','jtb.sh'])
		print "Don't wait, go and EXPLORE" 
	   	count = 1
		break
	elif show == 'Rampuria Haveli' or show == 'rampuria haveli':
		call(['bash','rh.sh'])
		count = 1
		print "Don't wait, go and EXPLORE" 
		break
	elif show == 'junaghar fort' or show == 'Junagahr Temple':
		call(['bash','jf.sh'])
		count = 1
		print "Don't wait, go and EXPLORE" 
		break
	elif show == 'Shri Laxminath Temple' or show == 'shri laxminath temple':
		call(['bash','slt.sh'])
	   	count = 1
		print "Don't wait, go and EXPLORE" 
		break
	else:
		print "***Please check the spelling and case***"
		count = 1
		break
os.system("python bikaner.py")
