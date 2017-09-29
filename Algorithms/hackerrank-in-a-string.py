#!/bin/python3

import sys

org = "hackerrank"
q = int(input().strip())
for a in range(0,q):
    s = input().strip()
    j = 0
    for i in range(0,len(s)):
        if org[j] == s[i] and j <= 9:
            j += 1
        if j == len(org):
            break
    if j == 10:
        print("YES")
    else:
        print("NO")
