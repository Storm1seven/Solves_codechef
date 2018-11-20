t = int(input())
for i in range(t):
	n, m, x, y = map(int, input().split())
	n-=1
	m-=1
	if (n%x == 0 and m%y == 0) or ((n-1)%x == 0 and (m-1)%y==0 and n>=1 and m >=1 ):
		print("Chefirnemo")
	else:
		print("Pofik") 