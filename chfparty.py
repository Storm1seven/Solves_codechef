for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    a.sort()
    for i in a:
        if count >= i:
            count+=1
    print(count)