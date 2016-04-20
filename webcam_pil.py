#!/usr/bin/env python
import os,time
import datetime
import opencv.adaptors
from opencv.cv import *
from opencv import highgui
import ImageEnhance
import Image
    
def get_image(camera):
    testimage = highgui.cvQueryFrame(camera)	
    time.sleep(1)
    im = highgui.cvQueryFrame(camera)
    dir(im)
    print "l'image est prise"
    return opencv.adaptors.Ipl2PIL(im)

a=os.popen('whoami')
l=a.read()
s=l.split('\n')
uname=s[0]
    
now = datetime.datetime.now()
now = str(now)
   
im=None
camera= highgui.cvCreateCameraCapture(1)
time.sleep(2)
im = get_image(camera)
os.chdir('/home/%s/Pictures' %(uname) )
fname='image_'+uname+"_"+now+'.png'
im.save(fname, "PNG")
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")
