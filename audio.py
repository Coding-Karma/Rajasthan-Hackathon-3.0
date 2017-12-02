# -*- coding: utf-8 -*-
import os                                                                                                
import sys                                                                                           
from subprocess import call
#logic = true
#while(true):
input=raw_input("Please interact\n")
if input is 'hello' or 'Hello' or 'Hey' or 'Hi' or 'hi' or 'hey':
        call(['bash','Hello-Female.sh'])
howdy=raw_input("Anything else?\n")
if input is 'how are you' or 'how are you?' or 'How are you?':
	call(['bash','fantastic.sh'])
        call(['bash','howareyou.sh'])
	random=raw_input("Now?\n")
	call(['bash','idk.sh'])
print "Please enter something"

