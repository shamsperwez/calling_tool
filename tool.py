#!/usr/bin/env python

import os

def firstCall():
    os.system('adb shell am start -a android.intent.action.CALL -d tel:+918298929363')

def secondCall():
    os.system('adb shell am start -a android.intent.action.CALL -d tel:+919798550770')

print('Calling Mursaleen or Vicky')
print('Choose the options 1 or 2 :')
val = int(input())
if val >= 0:
    if val == 1 :
        print('Calling Mursaleen')
        firstCall()
    if val == 2:
        print('Calling Vicky')
        secondCall()
        #pass
    #else :
     #   print('Next Time Better')
    #pass 
#else :
    #print('Thank You')

#os.system('adb devices')
#os.system("adb devices -l")
#os.system('adb shell getprop ro.build.version.release')
#os.system('adb usb')
#os.system('adb shell')