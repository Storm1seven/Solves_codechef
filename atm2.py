t = int(input())
for i in range(t):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	z = []
	for i in a:
		if k >= i:
			z.append('1')
			k-=i
		else:
			z.append('0')
	print("".join(z))