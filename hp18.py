for _ in range(int(input())):
	n, a, b = map(int, input().split())
	z = list(map(int, input().split()))
	common = 0
	count_a = 0
	count_b = 0
	for i in z:
	    if i%a == 0 and i%b == 0:
	        common+=1
	    elif i%a == 0:
	       	count_a+=1
	    elif i%b == 0:
	       	count_b+=1
	if a == b:
	    if common:
	    	print('BOB')
	    else:
	        print('ALICE')
	else:
		if count_b == count_a:
			if common:
				print('BOB')
			else:
				print('ALICE')
		elif count_a > count_b:
			print('BOB')
		else:
			print('ALICE')