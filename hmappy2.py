import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
for _ in range(int(input())):
    n, a, b, k = map(int, input().split())
    n+=1
    if n//a + n//b - 2*n//(lcm(a, b)) >= k:
        print('Win')
    else:
        print('Lose')