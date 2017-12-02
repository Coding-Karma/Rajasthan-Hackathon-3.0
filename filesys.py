import sys
import Tkinter
import tkFileDialog
import os
from subprocess import call
root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window
initdir=os.getcwd()
mydir='/usr/local/lib/python2.7/dist-packages/chatterbot_corpus/data/english/'

tempdir = tkFileDialog.askdirectory(parent=root, initialdir=mydir,title='Please select a directory')
os.makedirs(tempdir)
#if len(tempdir) > 0:
#   print "%s" % tempdir
#def process_files(self):
#    savedir = tkFileDialog.askdirectory(title='Select folder to save results')
#    os.makedirs(savedir)
