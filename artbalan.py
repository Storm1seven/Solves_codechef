from collections import defaultdict
for _ in range(int(input())):
    s = input()
    k = len(s)
    check = [0]*26
    for i in range(26):
        if k%(i+1) == 0:
            check[i] = i+1
    d = defaultdict(int)
    for i in s:
        d[i]+=1
    l = len(d)
    val = list(d.values())
    val.sort(reverse = True)
    ans = []
    for i in check:
        value = 0
        if i:
            if i < l:
                for j in val[:i]:
                    value+=abs(j-k//i)
                value+=sum(val[i:])
            elif i == l:
                for j in val:
                    value+=abs(j-k//i)
            else:
                for j in val:
                    value+=abs(j-k//i)
                value+=(i-l)*k//i
            ans.append(value)
    print(min(ans)//2)