t = int(input())
for i in range(t):
	n = int(input())
	count = 0
	for j in range(n):
		a, b = map(int, input().split())
		if b-a > 5:
			count+=1
	print(count)
