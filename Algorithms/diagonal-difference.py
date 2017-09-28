#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
pd = 0
for x in range(len(a)):
    pd += a[x][x]
i = 0
sd = 0
for y in reversed(range(len(a))):
    sd += a[i][y]
    i += 1
sum = pd - sd
print(abs(sum))
