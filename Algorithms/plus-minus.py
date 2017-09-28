#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
ne = po = ze = 0
for x in arr:
    if x < 0:
        ne += 1
    elif x == 0:
        ze += 1
    else:
        po += 1
to = len(arr)
print("%.6f" %float(po/to))
print("%.6f" %float(ne/to))
print("%.6f" %float(ze/to))
