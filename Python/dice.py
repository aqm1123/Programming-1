from matplotlib import pyplot as plt
from random import randint
import numpy as np

def roll():
	#This is fake and gay
	numbers_generated = []
	n = int(input("How many dice rolls? (100, 1000,  10000):  ")) 
	for i in range(n):
		
		a = randint(1,6)
		b = randint(1,6)
		
		numbers_generated.append(a+b)
			
	#sort list	
	numbers_generated = sorted(numbers_generated, key = int)
	
	#make dictionary of key (number) and value (frequency) 1
	frequency = {x:numbers_generated.count(x) for x in numbers_generated}
	
	#make a list out of the values of the dictionary for y-axis
	freq = list(frequency.values())
	print(frequency)
	#print(freq)
	#numbers for x_axis
	numbers_12 = []
	
	for x in range(2, 13):
		numbers_12.append(x)
	
	gausian_list = produce_gausian_list(n)
	#print(numbers_12)
	plt.bar(numbers_12, freq, align = 'center')
	plt.bar(numbers_12, gausian_list, align = 'center', width = 0.2)
	plt.xticks(np.arange(min(numbers_12), max(numbers_12)+1, 1))
	plt.yticks(np.arange(min(freq), max(freq)+1, y_axis_increment(n)))
	plt.xlabel('Numbers rolled')
	plt.ylabel('Frequency')
	plt.title('Frequency for {0} dice rolls'.format(str(n)))
	plt.legend(["Actual","Expected"])
	plt.axis(ymin=0)
	plt.grid()
	plt.show()
	


def y_axis_increment(n):
	if n <= 100:
		inc = 1
		return inc
	elif 10000 >= n > 1000:
		inc = n/(n/100)
		return inc
		
	elif n >= 100000:
		inc = n/(n/1000)
		return inc
		
	elif n == 1000:
		inc = n/100
		return inc
		
def produce_gausian_list(n):
	g_list = []
	
	for x in range(2,13):
		if x <= 7:
			y = n * ((x-1)/36)
			g_list.append(y)
		elif x > 7:
			y = n * ((13-x)/36)
			g_list.append(y)
			
	return g_list
	

			
roll()
		
	
	
	
		
