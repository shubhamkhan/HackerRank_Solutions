#!/bin/python3

import sys


n = int(input().strip())
for i in range(1,n+1):
    for j in range(0,n):
        if j >= n-i :
            print("#",end="")
        else:
            print(" ",end="")
    print("")
