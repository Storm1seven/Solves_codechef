for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        if b[i] - a[i-1] - a[(i+1)%n] > 0:
            c.append(b[i])
    if not c:
        print(-1)
    else:
        print(max(c))