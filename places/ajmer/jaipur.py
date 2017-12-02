import subprocess
import os
from subprocess import call
import sys,termios
print "The places you wanna visit in jaipur"
print "> Amber Palace"
print "> Hawa Mahal"
print "> Ganesha"
print "> Janter Mantar"
print "> Birla"
print "> JaiGarh"
print "> Govind Devi Ji"
print "> Jal Mahal" 
print "> Nahar Ghar"
print "> City Palace" 
#count = 0
show=raw_input("Please type the places you want to see before you go \n")
while 1:
	if show == 'Amber Palace' or show == 'amber palace':
		call(['bash','ap.sh'])
		print "Don't wait, go and EXPLORE" 
		count =1
		break
	elif show == 'Hawa Mahal' or show == 'hawa mahal':
		call(['bash','hm.sh'])
		print "Don't wait, go and EXPLORE" 
		count = 1
		break
	elif show == 'Ganesha' or show == 'ganesha':
		call(['bash','g.sh'])
		print "Don't wait, go and EXPLORE" 
	   	count = 1
		break
	elif show == 'Jantar Mahal' or show == 'jantar mantar':
		call(['bash','jm.sh'])
		count = 1
		print "Don't wait, go and EXPLORE" 
		break
	elif show == 'birla' or show == 'Birla':
		call(['bash','b.sh'])
		count = 1
		print "Don't wait, go and EXPLORE" 
		break
	elif show == 'Jai Ghar' or show == 'jai ghar':
		call(['bash','jg.sh'])
	   	count = 1
		print "Don't wait, go and EXPLORE" 
		break
	elif show == 'Govnind devi ji' or show == 'govind devi ji':
                call(['bash','gd.sh'])
                print "Don't wait, go and EXPLORE"
                count = 1
                break
        elif show == 'jal mahal' or show == 'Jal Mahal':
                call(['bash','jalm.sh'])
	        count = 1
                print "Don't wait, go and EXPLORE"
                break
        elif show == 'Nahar Ghar' or show == 'nahar ghar':
                call(['bash','ng.sh'])
                count = 1
                print "Don't wait, go and EXPLORE"
                break
        elif show == 'City Palace' or show == 'city palace':
                call(['bash','cp.sh'])
                count = 1
                print "Don't wait, go and EXPLORE"
                break
	else:
		print "***Please check the spelling and case***"
		count = 1
		break
os.system("python jaipur.py")

