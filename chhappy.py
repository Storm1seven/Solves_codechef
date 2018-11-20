t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	d = {}
	s = set(a)
	for i in range(n):
		d.setdefault(a[i], [])
		d[a[i]].append(i)
	z = {k:v for k, v in d.items() if len(v)>= 2}
	flag = False
	y = z.values()
	for i in y:
		for j in range(len(i)):
			if i[j]+1 in s:
				for k in range(j+1, len(i)):
					if i[k]+1 in s:
						flag = True
						break
			if flag:
				break
		if flag:
			break
	if flag:
		print('Truly Happy')
	else:
		print('Poor Chef')