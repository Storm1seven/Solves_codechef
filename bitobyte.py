n = int(input())
for _ in range(n):
	bit = 0
	nibble = 0
	byte = 0
	t = int(input())
	x = t//26
	y = t%26
	if y ==0:
		byte+=2**(x-1)
	else:
		bit+=2**x
	if y in range(3, 11):
		print(nibble, bit, byte)
	elif y in range(11,26):
		print(byte, nibble, bit)
	elif y in range(0, 3):
		print(bit, nibble, byte)

