#!/bin/python3

import sys

S = input().strip()
cnt = 0
L = "SOS"
for i in range(1,int(len(S)/3)):
    L = (L + "SOS")
for i in range(0,len(S)):
    if ord(S[i]) != ord(L[i]):
        cnt += 1
print(cnt)
