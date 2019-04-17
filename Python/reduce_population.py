#requirements:
# for 2 in population there is 1 kid
#all population starts at age 1
#kid  produced at age 25 
#age max is 80
#half female half male
#total population = initial population + deaths + births 
#amount of people giving births at a time is  = previous births
#deaths = last total ppulation - last populaton before birth
#deaths = last total ppulation - last populaton before birth	
from matplotlib import pyplot as plt

def population():

	n = 700
	y = 500
	
	#initial age of population
	age = 1
	
	#important values to measure total population
	deaths = [0]
	births = []
	initial_population = []

	#birth size for every 25 years
	birth_size = [n]

	#y-values for graph
	total_population = []
	#x-values for graph
	year = [0]
	
	for i in range(n):
		initial_population.append(i)

	total_population.append(len(initial_population))

	# how  many years gone by
	for i in range(1,y):


		#birth at 25
		if age % 25 == 0:
			newbirths = []
			if birth_size[-1] > 0:
				for x in range(1, birth_size[-1] +1):
					if x % 2 == 0:
						births.append(x)
						newbirths.append(x)
				birth_size.append(len(newbirths))
				
			else:
				birth_size = (birth_size)


		if age % 80 == 0:

			deaths.append(int(birth_size[0]))
			#remove that initial one everytime only above 0 because without a list there occurs an error
			if birth_size[0] > 0:
				del birth_size[0]
		
 
		total_population.append(len(births) + len(initial_population) - (sum(deaths)))
		
		age += 1
		year.append(i)
		print(str(i) + ": " + str(birth_size))
	
	
	
	print("Year" + "\tPopulation")
	for i in range(y):
		print(str(year[i]) + "\t" + str(total_population[i]))
		
	
	plt.plot(year, total_population)
	plt.xlabel("Year")
	plt.ylabel("Population")
	plt.title("Change of population")
	plt.show()
	

population()
