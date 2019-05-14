def removechar(s, i):
    return s[:i]+s[i+1:]
for _ in range(int(input())):
    n, d = input().split()
    while True:
        k = n
        n+=d
        z = [n]*len(n)
        for i in range(len(z)):
            z[i] = removechar(z[i], i)
        if k == min(z):
            break
        else:
            n = min(z)
    print(k)