from collections import defaultdict
t = int(input())
for i in range(0,t):
    n = int(input())
    a = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in a:
        if i%2==0:
            even+=1
        else:
            odd+=1
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    x = 0
    y = 0
    for i in a:
        x+= d[i^2]
    for i in a:
        y+=d[i^0]
    print(int(even*(even-1)/2 + odd*(odd-1)/2 - x/2 - (y-n)/2))