t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	h = list(map(int, input().split()))
	c = list(map(int, input().split()))
	h.reverse()
	c.reverse()
	m = 0
	z = []
	for i in range(n):
		if h[i] > m:
			z.append(c[i])
			m = h[i]
	print(len(set(z)))