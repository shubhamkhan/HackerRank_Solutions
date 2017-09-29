#!/bin/python3

import sys


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    re = 1
    if n == 0:
        print(1)
    else:
        for i in range(0,n):
            if i % 2 == 1:
                re += 1
            elif i % 2 == 0:
                re *= 2
        print(re)
