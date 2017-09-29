#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    p = 0
    for i in range(0,len(ar)):
        for j in range(i+1,len(ar)):
            if (ar[i]+ar[j]) % k == 0:
                #print(ar[i],"+",ar[j],"=",ar[i]+ar[j])
                p += 1
    return(p)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
