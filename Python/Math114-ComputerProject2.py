import math as m

function1 = lambda x: ((x)/(m.sin(x)))**2
DDF1 = lambda x: (((x)/(m.sin(x))) - ((2*m.cos(x)*(m.sin(x)-(x)*(m.cos(x))))/(m.sin(x)**3)))
NDDF1 = lambda x:  (2/(m.sin(x)**4))*(x**2 * m.cos(2*x) + 2*x**2 - 2*x*m.sin(2*x) - 0.5*m.cos(2*x)+0.5)
#((((2*(x**2)+2)*m.sin(x)**2)) - (8*x*m.cos(x)*m.sin(x)) + (6*(x**2)*m.cos(x)**2))/(m.sin(x)**4)
#((2*x**2+2)*(m.sin(x)**2) - (8*x*m.cos(x)*m.sin(x)) + (6*x**2*m.cos(x)**2))/(m.sin(x)**4) yyyyy
# ((2*(m.sin(x)-x*m.cos(x)))/m.sin(x)**3) - (6*x*m.cos(x)*(m.sin(x) - x*m.cos(x)))/m.sin(x)**4 + (2*x**2)/m.sin(x)**2 yyyyy
# 
#2*m.sinh(x)**2 * (x*(x*m.sinh(x)**2 + 2*x*m.tanh(x)**2 - 4*m.tanh(x)) + 1) (2*m.sinh(x)**2) - (8*x*m.sinh(x)**2 * m.tanh(x)) + (4*x**2 * m.sinh(x)**2 * m.tanh(x)**2) + (2*x**2 * m.sinh(x)**4) #
func_a_1 = 0.1
func_b_1 = m.pi / 2
#################################################################
function2  = lambda x: ((m.exp(x) - 1)/(m.sin(x)))**2
DDF2 = lambda x: (((6*m.exp(2*x)-6*m.exp(x)+2)*m.sin(x)**2) + ((8*m.exp(x)-8*m.exp(2*x))*m.cos(x)*m.sin(x)) + (6*m.exp(2*x) - 12*m.exp(x) +6)*m.cos(x)**2)/(m.sin(x)**4)
#((2*m.exp(x)-1)*(m.sin(x)**2) - (2*m.exp(x)*m.cos(x)*m.sin(x)) + (2*m.exp(x) - 2)*m.cos(x)**2)/(m.sin(x)**3)
NDDF2 = lambda x: (((6*m.exp(2*x) - 6*m.exp(x) + 2)*m.sin(x)**2) + ((8*m.exp(x) - 8*m.exp(2*x)) * m.cos(x) * m.sin(x)) + ((6*m.exp(2*x) - 12*m.exp(x) + 6)*m.cos(x)**2))/(m.sin(x)**4)
func_a_2 = 0.1
func_b_2 = m.pi / 2
#################################################################
function3 = lambda x: ((m.atan(x))/(x))**2
DDF3 = lambda x: ((2*m.atan(x))/((x)**3)) - (2/((x)**2 * ((x)**2 + 1))) - (2 / (((x)**2 + 1)**2))
NDDF3 = lambda x: (2*((3*(x**4) + 6*(x**2) + 3) * (m.atan(x)**2) + (-6*(x**3) - (4*x))*(m.atan(x)) + (x**2))/((x**4)*(((x**2)+1)**2)))
func_a_3 = 0.1
func_b_3 = 1

f0 = lambda x: (4 / (x**2 +1))


def simpson(function, a, b):


	n = 8
	
	Anew = 1
	Aold = 10
	while (abs(Aold-Anew)>0.00001):
		Aold = Anew
		n += 2
		dx = (b-a) / n
		H = 0
		for i in range(1, n+1, 2):
			xL = a+(i-1)*dx
			H += function(xL) + 4*function(xL + dx) + function(xL + 2*dx)

		Anew = (H * dx/3) * m.pi

	FinalN = n
	FinalSol = Anew 
	print('SIMPSON...', 'N:', FinalN, 'Solution:', FinalSol)

simpson(function1, func_a_1, func_b_1)


def Midpoint(function, a, b, DDF):

	Aold = 0
	n = 8
	dx = (b-a)/n
	H = 0

	for i in range(1, n+1):
	    xM = a + (i-0.5) * dx
	    H = H + function(xM)
	    
	Anew = H * dx + ((b-a) * ((dx**2))/24) * DDF((a+b)/2)

	while (abs(Aold-Anew)>0.00001):
	    Aold = Anew
	    n = n+2
	    dx = (b-a)/n
	    H = 0
	    for i in range(1, n+1):
	        xM = a + (i-0.5) * dx
	        H += function(xM)
	    
	    Anew = (H * dx + (b-a)*dx**2/24 * DDF((a+b)/2)**2) * m.pi


	FinalN = n
	FinalSol = Anew
	print('MIDPOINT...', 'N:', FinalN, 'Solution:', FinalSol, 'DDF:', DDF((a+b)/2))


Midpoint(function2, func_a_2, func_b_2, NDDF2)

def extended_simpson(a, b, function):
	
	n = 8
	
	Anew = 2
	Aold = 1
	
	while (abs(Aold-Anew)>0.00001):
		n = n+2
		diff = (b-a)/(n)

		diff_list = []
		for i in range(1, n+1):
			diff_list.append(diff*i)

		Aold = Anew
		
		dx = (b-a)/n
		H = 0
		interval = []
		for i in range(n):
			interval.append(dx * i)


		for i in range(4, n-3):
			H += function(a + interval[i])

		Anew = m.pi * (dx/48) * ((17*(function(a))) + (59*(function(a + diff_list[0]))) + (43*(function(a + diff_list[1]))) + (49*(function(a + diff_list[2]))) + (48*H) 
			+ (49*(function(a + diff_list[-4]))) + (43*(function(a + diff_list[-3]))) + (59*(function(a + diff_list[-2]))) + (17*(function(b))))

	
	print('EXTEDED SIMPSON...', 'N:', n, 'Solution:', Anew)
	

extended_simpson(func_a_2, func_b_2, function2)



