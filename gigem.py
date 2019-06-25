#! /usr/bin/env python3
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
import sys

w = (255, 255, 255)
r = (255, 0, 0)
b = (0, 0, 255)
o = (255, 165, 0)
g = (0, 255, 0)
v = (160, 32, 240)
y = (255, 255, 0)
if len(sys.argv)<2:
    print('usage: {} <n>'.format(sys.argv[0]))
    sys.exit(1)

n = int(sys.argv[1])

# count from 1 to n
for i in range(1,n+1):
    # if number is divisable by 3, say 'gig'
    if i % 15 == 0:
        print("gig 'em")
        pixels = [
            w, w, w, w, w, w, w, w,           
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
        ]
        
        sense.set_pixels(pixels)
        time.sleep(0.01)
        sense.clear()
        # if number is divisable by 5, say 'em'
    elif i% 5 == 0:
        print("'em")
        pixels = [
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
        ]
        
        sense.set_pixels(pixels)
        time.sleep(0.01)
        sense.clear()
    # if number is divisable by both, say 'gig em'
    elif i % 3 == 0:
        print('gig')
        pixels = [
            
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
        ]
        
        sense.set_pixels(pixels)
        time.sleep(0.01)
        sense.clear()
    else:
        print(i)
