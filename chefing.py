for _ in range(int(input())):
    n = int(input())
    z = []
    for _ in range(n):
        z.append(set(input()))
    inter = set.intersection(*z)
    print(len(inter))