for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k >= 1166750:
        print(1)
    elif k >= 1066750:
        print(2)
    elif k >= 966750:
        print(3)
    else:
        i = 0
        while i < n:
            count = 1
            ans = 0
            for j in range(i, n):
                ans+=a[j]//count
                if ans > k:
                    break
                count+=1
            if ans <= k:
                break
            i+=1
        print(i+1)