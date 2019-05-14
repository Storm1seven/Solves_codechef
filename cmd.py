import bisect
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = [0]+list(map(int, input().split()))
    dead = [0]*(n+1)
    ans = []
    for __ in range(q):
        i, k = map(int, input().split())
        dead[i]+=1
        j = bisect.bisect(a, k)
        if j < n+1:
            while dead[j]:
                j+=1
                if j == n+1:
                    break
            if j == n+1:
                ans.append(-1)
            else:
                ans.append(j)
        else:
            ans.append(-1)
    print(*ans)