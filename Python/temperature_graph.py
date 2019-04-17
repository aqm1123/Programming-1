from matplotlib import pyplot as plt


def draw(x, y):
	x_numbers = x
	y_numbers = y
	
	plt.plot(x_numbers, y_numbers, marker = 'o')
	plt.title("Weather Barcelona today")
	plt.xlabel("Time")
	plt.ylabel("Temperature")
	plt.axis(ymax = 30, xmax = 24)
	
def weather_bcn():
	time_x = []
	
	for t in range(24):
		if t < 10:
			hour = "0{0}:00".format(str(t))
			time_x.append(hour)
		elif t >= 10:
			hour = "{0}:00".format(str(t))
			time_x.append(hour)
			
		
	print((time_x))
	
	temperature_y = [0, 2, 4, 5, 6, 6, 6, 7, 9, 10, 11, 12, 16, 23, 25, 25, 25, 23, 22, 18, 14, 12, 11, 2]
	#print(len(temperature_y))
	draw(time_x, temperature_y)
	plt.show()
	
	
weather_bcn()
