for _ in range(int(input())):
    n = int(input())
    s = set([])
    for __ in range(n):
        l = list(map(int, input().split()))
        s.add(l[0])
        s.add(l[1])
        s.add(l[2])
    l = list(s)
    l.sort()
    if l[0] == -1:
        l = l[1:]
    print(*l)