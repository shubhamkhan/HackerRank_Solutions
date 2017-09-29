#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
z = []
for x in range(0,len(word)):
    if ord(word[x]) >= 97 and ord(word[x]) <=122:
        l = ord(word[x]) - 97
    elif ord(word[x]) >=65 and ord(word[x]) <= 90:
        l = ord(word[x]) - 65
    z.append(h[l])
    mx = max(z)
print(mx*len(word))
