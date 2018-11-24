def daynum(a):
	if a == 'sunday':
		return 0
	elif a == 'monday':
		return 1
	elif a == 'tuesday':
		return 2
	elif a == 'wednesday':
		return 3
	elif a == 'thursday':
		return 4
	elif a == 'friday':
		return 5
	else:
		return 6
for _ in range(int(input())):
	s, e, l, r = input().split()
	s = daynum(s)
	e = daynum(e)
	l, r = int(l), int(r)
	if e - s < 0:
		diff = 7 + e - s + 1
	else:
		diff = e - s + 1
	z = []
	i = diff
	while i <= 100:
		z.append(i)
		i+=7
	count = 0
	for i in z:
		if i in range(l, r+1):
			num = i
			count+=1
	if count == 1:
		print(num)
	elif count == 0:
		print('impossible')
	else:
		print('many') 