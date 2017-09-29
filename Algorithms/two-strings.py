#!/bin/python3

import sys

def twoStrings(s1, s2):
    if len(s1) > len(s2):
        for i in s2:
            if i in s1:
                return("YES")
        else:
            return("NO")
    else:
        for i in s1:
            if i in s2:
                return("YES")
        else:
            return("NO")

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
