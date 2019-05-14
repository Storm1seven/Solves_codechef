for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cpos, cz, cneg = [0]*3
    for i in a:
        if i > 0:
            cpos+=1
        elif i == 0:
            cz+=1
        else:
            cneg+=1
    if cpos == n or cneg == n or cz == n:
        print(n, n)
    else:
        print(max(cpos, cneg)+cz, min(cpos, cneg))