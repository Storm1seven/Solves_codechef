import numpy
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(k, n+1):
    print(numpy.std(a[i-k:i]))
print()