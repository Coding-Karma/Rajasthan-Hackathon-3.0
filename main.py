from tkinter import *
import tkinter as tk
import os
import sys
from subprocess import call

root = Tk()
root.title("Smart Bot")
root.minsize(300,300)
root.geometry("500x500")
thelabel = Label(root,text="Innovate & Secure")
thelabel.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
thelabel.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

def quit():
	root.destroy()

def trans():
	call(['bash', 'input.sh'])
def Location():
	os.system('python find_location.py')
	call(['bash', 'cityfind.sh'])
def Search():
	call(['bash', 'google.sh'])
def Interact():
	os.system('python chatme.py')
def Help():
	os.system('python help.py')
def Teachme():
	print "Please append the name of your directory at the end of the path"
	
	os.system('python filesys.py')
	
	call(['bash','learn.sh'])
def Talk():
	os.system('python audio.py')
def pron():
	print "Spanish Sample"
	call(['bash','spain.sh'])
	print "French Sample"
	call(['bash','france.sh'])
	print "Chinese Sample"
	call(['bash','chinese.sh'])

def verbose():
	os.system('python verbose')
def Places():
	print "Places we suggest out of famous cities"
	os.system('python ajmer.py')
	os.system('python jaipur.py')
	os.system('python jaisalmer.py')
	os.system('python jodhpur.py')
	os.system('python bikaner.py')
	os.system('python udaipur.py')
def food():
	print "Some tempting dishes you must have in rajasthan"
	os.system('python food.py')
button1 = Button(bottomFrame,text = "exit",command = quit)
button2 = Button(topFrame, text = "Translate",command = trans)
button3 = Button(topFrame,text="Locate",command=Location)
button4 = Button(topFrame,text="Explore your location",command=Search)
button5 = Button(topFrame,text="Interact",command=Interact)
button6 = Button(topFrame,text="My Introduction",command=Help)
button7 = Button(topFrame,text="Teach Me",command=Teachme)
button8 = Button(topFrame,text="I can talk",command=Talk)
button9 = Button(topFrame,text="Language-Detection",command=pron)
button11 = Button(topFrame,text="Verbose",command=verbose)
button12 = Button(topFrame,text="Suggested Places",command=Places)
button13= Button(topFrame,text="Suggested Food",command=food)
#button13= Button(topFrame,text="Ajmer")
#button14= Button(topFrame,text="Bikaner")
#button15= Button(topFrame,text="Jaipur")
#button16= Button(topFrame,text="Jaisalmer")
#button17= Button(topFrame,text="Jodhpur")
#button18= Button(topFrame,text="Udaipur")

thelabel.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
thelabel.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button11.pack()
button8.pack()
button9.pack()
button12.pack()
button13.pack()
root.mainloop()
