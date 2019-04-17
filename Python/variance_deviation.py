""" find the variance and standard deviation of a list of numbers """

def calculate_mean(numbers):
	
	sum_numb = sum(numbers)
	len_numb = len(numbers)
	
	mean = sum_numb / len_numb
	
	return mean
	
def find_difference(numbers):
	
	mean = calculate_mean(numbers)
	
	diff = []
	
	for x in numbers:
		diff.append(x - mean)
		
	return diff
	
def main():
	
	numbers = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
	
	differences = find_difference(numbers)
	
	sqd_diff = []
	
	for d in differences:
		sqd_diff.append(d**2)
		
		
	variance = sum(sqd_diff)/len(numbers)
	
	std_deviation = variance**0.5
	
	print("Variance: {0} Standard Deviation: {1}".format(variance, std_deviation))
		

main()
	
	
