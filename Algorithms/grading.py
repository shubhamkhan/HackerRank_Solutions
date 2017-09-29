#!/bin/python3

import sys

n = int(input().strip())
for i in range(n):
    grades_t = int(input().strip())
    if grades_t % 5 >= 3 and grades_t > 36:
        if (grades_t % 5) == 3:
            grades_t += 2
        if (grades_t % 5) == 4:
            grades_t += 1
    print(grades_t)
