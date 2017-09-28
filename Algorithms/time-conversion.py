#!/bin/python3

import sys

time = input().strip()
h = time[0:2]
m = time[3:5]
s = time[6:8]
pm = time[8:10]
if pm == "PM":
    if int(h) != 12:
        h = int(h) + 12
    h = str(h)
elif pm == "AM":
    if int(h) == 12:
        h = '00'
print(h+":"+m+":"+s)
