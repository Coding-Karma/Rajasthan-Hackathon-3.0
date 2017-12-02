import os
import sys
import subprocess
from subprocess import call
import sys, termios
print "A list of food that we recommend while you are in Rajasthan \n"
print "> Dal Bati Churma"
print "> Laal Maas"
print "> Gatte ki Khichdi"
print "> Rajasthani Kadi"
print "> Gatte ka Pulao"
print "> Churma Ladoo"
print "> Badam ka Halwa"
print "> Gujia"
print "I can show you a few food images"
show=raw_input("What do you want to see? \n")
while 1:
	count = 0
	if show == 'Gujia' or show == 'gujia': 
		print"What are you waiting for,Don't be away from the tempting FOOD!"     
		call(['bash','gujia.sh'])
		count=1
		break
	elif show == 'Dal Bati Churma' or show == 'dal bati churma':
		print"What are you waiting for,Don't be away from the tempting FOOD!"     
		call(['bash','dbc.sh'])
		count =1
		break
	elif show == 'Laal Maas' or show == 'laal maas' or show == 'lal maas':
		print"What are you waiting for,Don't be away from the tempting FOOD!"     
		call(['bash','lm.sh'])	
		count =1
		break	
	elif show == 'Gatte ki Khichdi' or show == 'gatte ki khichdi':
	        print"What are you waiting for,Don't be away from the tempting FOOD!"     	
		call(['bash','gkk.sh'])
		count =1
		break
	elif show == 'Rajasthani Kadi' or show == 'rajasthani kadi':
		print"What are you waiting for,Don't be away from the tempting FOOD!"     
		call(['bash','rk.sh'])
		count =1
		break
	elif show == 'Gatte ka Pulao' or show == 'gatte ka pulao':
		print"What are you waiting for,Don't be away from the tempting FOOD!"     	
		call(['bash','gkp.sh'])
		count =1
		break
	elif show == 'Churma Ladoo' or show == 'churma ladoo':
		print"What are you waiting for,Don't be away from the tempting FOOD!"
		call(['bash','cl.sh'])
		count =1
		break
	elif show == 'Badam ka Halwa' or show == 'badam ka halwa':
		print"What are you waiting for,Don't be away from the tempting FOOD!"     
		call(['bash','bkh.sh'])
		count =1
		break
	else: 
		print "I am not sure what you want?"
		count =1
		break
if(count == 1):
	os.system('python food.py')

