t = int(input())
for i in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	z = 0
	for i in set(a):
		if i <= n:
			z+=1
	print(n-z)