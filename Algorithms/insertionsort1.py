#!/bin/python3

import sys

n = int(input().strip())
ar = list(map(int, input().strip().split(" ")))
for k in range(0,n-1):
    for i in range(0,n-1):
        if ar[i] > ar[i+1]:
            temp = ar[i+1]
            ar[i+1] = ar[i]
            for j in ar:
                print(j, end=" ")
            ar[i] = temp
            print()
for j in ar:
    print(j, end=" ")
