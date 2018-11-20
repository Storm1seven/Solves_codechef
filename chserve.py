t = int(input())
for _ in range(t):
	p1, p2, k = map(int, input().split())
	if ((p1+p2)//k)%2 == 0:
		print('CHEF')
	else:
		print('COOK')