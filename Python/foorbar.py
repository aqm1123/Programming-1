def action(index):
	
	prime_numbers = ["2"]
	checker = 0
	
	#create primer numbers
	for x in range(3, 1001):
		for y in range(2, x):
			if x % y == 0:
				break
			else:
				checker += 1
		if checker == (x-2):
			prime_numbers.append(str(x))
		checker = 0
	
	#print(prime_numbers)
	long_string_numbers = "".join(prime_numbers)
	#print(long_string_numbers)
	print(long_string_numbers[int(index):int(index) + 5])
	
	
	
	
action(123)
			
	
	
	
	


