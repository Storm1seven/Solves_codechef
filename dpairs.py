from sys import stdin, stdout
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
n, m = mapin()
a = listin()
b = listin()
s = set([])
index1 = a.index(max(a))
index2 = b.index(min(b))
for i in range(n):
	print(i, index2)
for i in range(m):
	if i != index2:
		print(index1, i)