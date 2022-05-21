#!/usr/bin/env python

import os

def firstCall():
    os.system('adb shell am start -a android.intent.action.CALL -d tel:+91xxxxxxxxxx') #put your friend_1 mobile number here

def secondCall():
    os.system('adb shell am start -a android.intent.action.CALL -d tel:+91xxxxxxxxxx') #put your friend_2 mobile number here

print('Calling Friend_1 or Friend_2') #you can change your friend name here
print('Choose the options 1 or 2 :')
val = int(input())
if val >= 0:
    if val == 1 :
        print('Calling Friend_1')
        firstCall()
    if val == 2:
        print('Calling Friend_2')
        secondCall()
  
