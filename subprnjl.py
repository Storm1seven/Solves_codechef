from bisect import insort
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        counter = [0]*2001
        current = []
        length = 0
        for j in range(i, n):
            insort(current, a[j])
            length+=1
            counter[a[j]]+=1 
            repeat = (k+length-1)//length
            index = k//repeat
            if k%repeat == 0:
                index-=1
            if counter[counter[current[index]]]:
                ans+=1
    print(ans)