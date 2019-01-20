for _ in range(int(input())):
    n, p = map(int, input().split())
    maxrem = n//2 - int(n%2 == 0)
    if n == 1:
        print(p**3)
        continue
    print((p-maxrem)**2+(p-n)*(p - maxrem)+(p-n)**2)