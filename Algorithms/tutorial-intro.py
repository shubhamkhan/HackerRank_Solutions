V = int(input())
n = int(input())
ar = list(map(int, input().strip().split(" ")))
for i in range(0,len(ar)):
    if V == ar[i]:
        print(i)
        break
