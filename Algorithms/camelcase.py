#!/bin/python3

import sys


s = input().strip()
cnt = 1
for i in range(0,len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <=90:
        cnt += 1
print(cnt)
