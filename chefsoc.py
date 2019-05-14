from collections import deque
for _ in range(int(input())):
    n = int(input())
    a = input().split()
    a = ''.join(a)
    ans = 0
    q = deque([({0}, 0)])
    while q:
        current = q.popleft()
        last = current[1]
        current = current[0]
        ans+=1
        if a[last] == '1':
            if last-1 >= 0:
                if last-1 not in current:
                    current.add(last-1)
                    q.append((current, last-1))
            if last+1 < n:
                if last+1 not in current:
                    current.add(last+1)
                    q.append((current, last+1))
        else:
            if last-1 >= 0:
                if last-1 not in current:
                    current.add(last-1)
                    q.append((current+last-1))
            if last+1 < n:
                if last+1 not in current:
                    current.add(last+1)
                    q.append((current, last+1))
            if last-2 >= 0:
                if last-2 not in current:
                    current.add(last-2)
                    q.append((current, last-2))
            if last+2 < n:
                if last+2 not in current:
                    current.add(last+2)
                    q.append((current, last+2))
    print(ans%(1000000007))