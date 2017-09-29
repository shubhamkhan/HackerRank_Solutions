#!/bin/python3

import sys

def funnyString(s):
    r = list(reversed(s))
    f = 0
    for i in range(1,len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) == abs(ord(r[i]) - ord(r[i-1])):
            continue
        else:
            f = 1
            break
    if f == 0:
        return("Funny")
    else:
        return("Not Funny")

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
