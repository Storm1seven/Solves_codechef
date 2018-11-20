from fractions import Fraction as f
a = list(map(int, input().split()))
t = a[0]
a = a[1:]
z = [f(1, 2), f(1, 4)]
for i in range(2, 25):
	z.append((z[i-1]+z[i-2])/2)
for i in a:
	print(z[i-1].numerator, z[i-1].denominator, end = " ")
print()