import math as m
f = lambda x: (54*(x**6) + 45*(x**5) - 102*(x**4) - 69*(x**3) + 35*(x**2) + 16*x - 4) 
deriv = lambda x: (324*(x**5) + 225*(x**4) - 408*(x**3) - 207*(x**2) + 70*x + 16)

def newton(a, i):
	b = 0
	it = 0
	for r in range(i): 
		y = f(a)
		dy = deriv(a)
		b = a - ((float) (y) / dy)
		if abs(a - b) < 0.0001: 
			break
		a = b
		it += 1
	return b, it





print(newton(2, 30))










