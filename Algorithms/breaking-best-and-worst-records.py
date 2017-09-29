#!/bin/python3

import sys

def getRecord(s):
    l = 0
    h = 0
    md = s[0]
    re = []
    ho = md
    lo = md
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    for i in range(0,len(t)):
        if t[i] > md and t[i] > ho:
            h += 1
            ho = t[i]
        elif t[i]< md and t[i] < lo:
            l += 1
            lo = t[i]
    re = [h,l]
    return(re)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
for i in result:
    print(i,end=" ")
