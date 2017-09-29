#!/bin/python3

import sys

def solve(n, s, d, m):
    cnt = 0
    for i in range(0,n):
        add = 0
        if i+m <= n:
            for j in range(i,i+m):
                add += s[j]
            if add == d:
                    cnt += 1
    return(cnt)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
