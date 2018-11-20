t = int(input())
for _ in range(t):
	z = []
	n = int(input())
	for i in range(n):
		x, y = map(int, input().split())
		z.append((x-2,y+1))
		z.append((x-2,y-1))
		z.append((x-1,y+2))
		z.append((x+1,y+2))
		z.append((x+2,y+1))
		z.append((x+2,y-1))
		z.append((x+1,y-2))
		z.append((x-1,y-2))
	p, q = map(int, input().split())
	y = list(set(z))
	if (p, q) not in z:
		print('NO')
	else:
		if (p+1,q+1) and (p+1,q) and (p+1,q-1) and (p,q-1) and (p-1,q-1) and (p-1,q) and (p-1,q+1) and (p, q+1) in y:
			print('YES')
		else:
			print('NO')
