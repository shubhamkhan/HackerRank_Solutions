#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
app = 0
ora = 0
for i in apple:
    lo = a+i
    if lo >= s and lo <= t:
        app += 1
for i in orange:
    lo = b+i
    if lo >= s and lo <= t:
        ora += 1
print(app)
print(ora)
