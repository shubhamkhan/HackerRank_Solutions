import math
t = int(input())
for i in range(t):
    a, b = input().strip().split(" ")
    a = int(a)
    b = int(b)
    
    stA = math.ceil(math.sqrt(a))
    stB = math.floor(math.sqrt(b))
    
    print(stB - stA + 1)
