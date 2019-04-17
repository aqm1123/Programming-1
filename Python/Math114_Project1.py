import math as m
f0 = lambda x: (4 / (x**2 +1))
f1 = lambda x: ((2.85*x) - 1.47)
f2 = lambda x: (2*m.exp(-x**2))

n = [2, 10, 100, 1000, 50000]
a = 0.196
f0_b = 1
f1_b = 0.771

def change_x(a, b, n):

	n_list = n 
	x_change = []

	for n in n_list:
		x_change.append((b-a)/int(n))

	return x_change

delta_x0 = change_x(a, f0_b, n)
delta_x1 = change_x(a, f1_b, n)

# print(delta_x0, delta_x1)
# print(len(delta_x0), len(delta_x1))

def left_rule(a, delta_x0, delta_x1, f0, f1, f2, n):
	#calculate areas for every N value for each function annd then append to the lists. 
	area0_list = []
	area1_list = []
	area2_list = []

	for x in range(5):
		h2 = 0
		h1 = 0
		h0 = 0
		for i in range(1, n[x]+1):
		
			xL = a + (i-1)*(delta_x0[x])
			xL1 = a + (i-1)*(delta_x1[x])
			h0 += f0(xL)
			h1 += f1(xL1)
			h2 += f2(xL)

		area = h0 * delta_x0[x]
		area0_list.append(area)		

		area1 = h1 * delta_x1[x]
		area1_list.append(area1)

		area2 = h2 * delta_x0[x]
		area2_list.append(area2)


	print("LR AREA0 LIST = " + str(area0_list) + "\n\n" + "LR AREA1 LIST = " + str(area1_list) + "\n\n" + "LR AREA2 LIST = " + str(area2_list) + "\n\n")
	



def right_rule(a, delta_x0, delta_x1, f0, f1, f2, n):
	#calculate areas for every N value for each function annd then append to the lists. 
	area0_list = []
	area1_list = []
	area2_list = []

	for x in range(5):
		h2 = 0
		h1 = 0
		h0 = 0
		for i in range(1, n[x]+1):
		
			xR = a + (i * delta_x0[x])
			xR1 = a + (i * delta_x1[x])
			h0 += f0(xR)
			h1 += f1(xR1)
			h2 += f2(xR)

		area = h0 * delta_x0[x]
		area0_list.append(area)		

		area1 = h1 * delta_x1[x]
		area1_list.append(area1)

		area2 = h2 * delta_x0[x]
		area2_list.append(area2)


	print("RR AREA0 LIST = " + str(area0_list) + "\n\n" + "RR AREA1 LIST = " + str(area1_list) + "\n\n" + "RR AREA2 LIST = " + str(area2_list) + "\n\n")


def mid_rule(a, delta_x0, delta_x1, f0, f1, f2, n):
	area0_list = []
	area1_list = []
	area2_list = []

	for x in range(5):
		h2 = 0
		h1 = 0
		h0 = 0
		for i in range(1, n[x]+1):
		
			xL = (a + (i-1)*(delta_x0[x])) + (delta_x0[x] / 2)
			xL1 = (a + (i-1)*(delta_x1[x])) + (delta_x0[x] / 2)
			h0 += f0(xL)
			h1 += f1(xL1)
			h2 += f2(xL)

		area = h0 * delta_x0[x]
		area0_list.append(area)		

		area1 = h1 * delta_x1[x]
		area1_list.append(area1)

		area2 = h2 * delta_x0[x]
		area2_list.append(area2)


	print("MR AREA0 LIST = " + str(area0_list) + "\n\n" + "MR AREA1 LIST = " + str(area1_list) + "\n\n" + "MR AREA2 LIST = " + str(area2_list) + "\n\n")



def trapezoid(a, delta_x0, delta_x1, f0, f1, f2, n):

	area0_list = []
	area1_list = []
	area2_list = []

	for x in range(5):
		h2 = 0
		h1 = 0
		h0 = 0
		for i in range(1, n[x]+1):
		
			xL = a + (i-1)*(delta_x0[x])
			xR = a + (i * delta_x0[x])
			xL1 = a + (i-1)*(delta_x1[x])
			xR1 = a + (i * delta_x1[x])
			h0 += f0(xL) + f0(xR)
			h1 += f1(xL1) + f1(xR1)
			h2 += f2(xL) + f2(xR)

		area = h0 * (delta_x0[x] / 2)
		area0_list.append(area)		

		area1 = h1 * (delta_x1[x] / 2)
		area1_list.append(area1)

		area2 = h2 * (delta_x0[x] / 2)
		area2_list.append(area2)

	print("Trapezoid AREA0 LIST = " + str(area0_list) + "\n\n" + "Trapezoid AREA1 LIST = " + str(area1_list) + "\n\n" + "Trapezoid AREA2 LIST = " + str(area2_list) + "\n\n")

trapezoid(a, delta_x0, delta_x1, f0, f1, f2, n)


def simpson(a, f0_b, f1_b, f0, f1, f2, n):

	f1_h = []

	for x in n:
		H = (f1_b - a) / x
		f1_h.append(H)

	f0_h = []

	for x in n:
		H = (f0_b - a) / x
		f0_h.append(H)



	s0 = f0(a) + f0(f0_b)
	s1 = f1(a) + f1(f1_b)
	s2 = f2(a) + f2(f0_b)

	area0 = []
	area1 = []
	area2 = []

	for x in n:
		if x == n[0]:
			o = 0

		if x == n[1]:
			o = 1
		if x == n[2]:
			o = 2
		if x == n[3]:
			o = 3
		if x == n[4]:
			o = 4


		s0 = 0
		s1 = 0
		s2 = 0
		for i in range(1, x, 2):
			s0 += 4 * f0(a + i * f0_h[o])
			s1 += 4 * f1(a + i * f1_h[o])
			s2 += 4 * f2(a + i * f0_h[o])
		for i in range(2, x-1, 2):
			s0 += 2 * f0(a + i * f0_h[o])
			s1 += 2 * f1(a + i * f1_h[o])
			s2 += 2 * f2(a + i * f0_h[o])

		A0 = ((s0 + f0(a) + f0(f0_b)) * f0_h[o]) / 3
		A1 = ((s1 + f1(a) + f1(f1_b)) * f1_h[o]) / 3
		A2 = ((s2 + f2(a) + f2(f0_b)) * f0_h[o]) / 3
		
		area0.append(A0)
		area1.append(A1)
		area2.append(A2)

	print("Simpson 0 = " + str(area0) + "\n\n" + 'Simpson 1 = ' + str(area1) + "\n\n" + 'Simpson 2 = ' + str(area2))



simpson(a, f0_b, f1_b, f0, f1, f2, n)	
















