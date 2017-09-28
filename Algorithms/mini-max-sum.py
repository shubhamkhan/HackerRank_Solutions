#!/bin/python3

import sys
arr = list(map(int, input().strip().split(' ')))
list.sort(arr)
mx = sum(arr) - arr[0]
mi = sum(arr) - arr[-1]
print(mi,mx)
