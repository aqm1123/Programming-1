from matplotlib import pyplot as plt
import math

def frange(start, final, increment):
	numbers = []
	while start < final:
		numbers.append(start)
		start += increment 
		
	return numbers
	
def draw_graph(x, y):
	plt.plot(x, y)
	plt.xlabel("x_displacement")
	plt.ylabel("y-displacement")
	plt.title("Projectile motion of ball")
	
def draw_trajectory(u, theta):
	
	theta = math.radians(theta)
	print(theta)
	g = 9.8
	
	#time of flight
	t_flight = 2*u*math.sin(theta)/g
	
	#fined time intervals
	intervals = frange(0, t_flight, 0.00001)
	
	#list of x and y coordinates
	x = []
	y = []
	for t in intervals:
		x.append(u*math.cos(theta)*t)
		y.append(u*math.sin(theta)*t - 0.5*g*t*t)
		
	draw_graph(x, y)
	
def start():
	inputs = []
	angle = []
	try:
		u = float(input("Enter the initial velocity of object 1 (m/s): "))
		inputs.append(u)
		angle_1 = float(input("At what angle?: "))
		angle.append(angle_1)
		u1 = float(input("Enter the initial velocity of object 2 (m/s): "))
		inputs.append(u1)
		angle_2 = float(input("At what angle?: "))
		angle.append(angle_2)
		u2 = float(input("Enter the initial velocity of object 3 (m/s): "))
		inputs.append(u2)
		angle_3 = float(input("At what angle?: "))
		angle.append(angle_3)
		
		
	except ValueError:
		print("You entered an invalid input")
	
	else:
		for x in range(3):
			draw_trajectory(inputs[x], angle[x])
	
		plt.legend([u, u1, u2])
		plt.show()
	
start()



