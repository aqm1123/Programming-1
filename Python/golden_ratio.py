from matplotlib import pyplot as plt

def fibo(n):
	if n == 1:
		return [1]
	
	if n == 2:
		return [1, 1]
		
	a = 1
	b = 1
	series = [1, 1]
	for i in range(n):
		c = a + b
		series.append(c)
		a = b 
		b = c
	
	return series
	
	
def ratio_g(n):
	series = fibo(n)
	ratio_list = []
	for x in range(n):
		x1 = x + 1
		ratio = float(series[x1] / series [x])
		ratio_list.append(ratio)
		
	
	return ratio_list
	
def ratio_graph():
	
	n = 50
	y_axis = ratio_g(n)
	x_axis = []
	for n in range(n):
		x_axis.append(n)
		
	plt.plot(x_axis, y_axis)
	plt.title("Golden Ratio")
	plt.xlabel("Number")
	plt.ylabel("Ratio")
	#print(y_axis[-2])
	print(y_axis[-1])
	
	plt.show()
	
	
ratio_graph()
