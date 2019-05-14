for _ in range(int(input())):
    n, b = map(int, input().split())
    m = 0
    for __ in range(n):
        x, y, c = map(int, input().split())
        if c <= b:
            if x*y > m:
                m = x*y
    if m:
        print(m)
    else:
        print('no tablet')