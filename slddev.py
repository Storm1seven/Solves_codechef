n, k = map(int, input().split())
a = list(map(int, input().split()))
z = [i**2 for i in a]
a = [0]+a
z = [0]+z
for i in range(1, n+1):
    a[i]+=a[i-1]
    z[i]+=z[i-1]
print(a, z)
for i in range(k, n+1):
    print(a[i-k: i+1])
    s = a[i] - a[i-k]
    x_bar = s/k
    s_square = z[i] - a[i-k]
    ans = s_square + k*(x_bar)**2 - 2*x_bar*(s)
    ans/=k
    ans**=0.5
    print(ans, end = ' ')
print()