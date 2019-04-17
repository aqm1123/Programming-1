
#requirements:
# for 2 in population there is 1 kid
#all population starts at age 1
#kid  produced at age 25 
#age max is 80
#half female half male
#total population = initial population + deaths + births 
#amount of people giving births at a time is  = previous births
#deaths = last total ppulation - last populaton before birth

from matplotlib import pyplot as plt

def population():

	#initial age of population
	age = 2
	
	#important values to measure total population
	deaths = [0]
	births = []
	initial_population = []

	#birth size for every 25 years
	birth_size = [700]

	#y-values for graph
	total_population = []
	#x-values for graph
	year = [0]
	
	for i in range(700):
		initial_population.append(i)

	total_population.append(len(initial_population))

	# how  many years gone by
	for i in range(1,81):


		#birth at 25
		if age % 25 == 0:
			newbirths = []
			
			for x in range(birth_size[-1]):
				if x % 2 == 0:
					births.append(x)
					newbirths.append(x)
			birth_size.append(len(newbirths))


		#deaths = last total ppulation - last populaton before birth	

		if age % 80 == 0:

			deaths.append(int(birth_size[0]))
			#remove that initial one everytime
		
 
		total_population.append(len(births) + len(initial_population) - int((deaths[-1])))

		age += 1
		year.append(i)

	print("babys = " + str(len(births)))
	print("initial pop = " + str(len(initial_population)))
	print("total population = " + str((total_population)))
	print("Years = " + str(year))
	print("Deaths = " + str(deaths))
	print(len(total_population))
	print(len(year))

	plt.plot(year, total_population)
	plt.xlabel("Year")
	plt.ylabel("Population")
	plt.tile("Change of population")
	plt.show()
	

population()

