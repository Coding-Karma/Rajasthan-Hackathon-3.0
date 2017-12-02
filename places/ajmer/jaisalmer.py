import subprocess
import os
from subprocess import call
import sys, termios
print "The places you want to visit in Jaisalmer"
print "> bada bagh jaisalmer"
print "> jain temples jaisalmer "
print "> gadisar lake jaisalmer"
print "> jaisalmerfort"
count = 0
show= raw_input("Please type the places you want to see in Jaisalmer\n")
while 1:
	if show == 'Bada Bagh Jaisalmer' or show == 'bada bagh jaisalmer':
		call(['bash','bbj.sh'])
		print "Don't wait, go and explore"
		count=1
		break
	elif show == 'Jain Temples Jaisalmer' or show == 'jain temples jaisalmer':
		call(['bash','jtj1.sh'])
		print "Don't wait, go and explore"
		count=1
		break
	elif show == 'Gadisar Lake Jaisalmer' or show == 'gadisar lake jaisalmer':
		call(['bash','glj.sh'])
		print "Don't wait, go explore"
		count=1
		break
	elif show ==  'JaisalmerFort' or show == 'jaisalmerfort':
		call(['bash','jf2.sh'])
		print "Don't wait, go explore"
		count=1
		break
	else:
		print "***please check the spelling and case***"
		count=1
		break
os.system("python jaisalmer.py")

