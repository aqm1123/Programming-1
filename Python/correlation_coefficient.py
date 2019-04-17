""" calculatin correlation coefficient """

from matplotlib import pyplot as plt

def main():
	
	
	list1 = [1, 2, 3, 4, 5]
	list2 = [1, 2, 5, 3, 5]
	
	cc = (len(list1) * calculate_sumXY(list1, list2) - (sum_list1(list1) * sum_list2(list2))) / ((((len(list1)*sum_list1_sqd(list1)) - (sum_list1(list1)**2)) * ((len(list1)*sum_list2_sqd(list2)) - (sum_list2(list2)**2)))**0.5)
	
	print(cc)
	
	plt.scatter(list1, list2)
	plt.xlabel("X-axis")
	plt.ylabel("Y-axis")
	plt.title("Title")
	plt.legend(str(cc))
	plt.show()
	
			
def calculate_sumXY(list1, list2):
	
	sum_product_XY = []
	
	for x, y in zip(list1, list2):
		
		sum_product_XY.append(x * y)
		
	
	return sum(sum_product_XY)
		
		
def sum_list1(list1):
	
	sum_list1 = sum(list1)
	
	return sum_list1
	
def sum_list2(list2):
	
	sum_list2 = sum(list2)
	
	return sum_list2
	
	
def sum_list1_sqd(list1):
	
	list1_sqd = []
	
	for x in list1:
		list1_sqd.append(x**2)
		
	return sum(list1_sqd)
	
def sum_list2_sqd(list2):
	
	list2_sqd = []
	
	for x in list2:
		list2_sqd.append(x**2)
		
	return sum(list2_sqd)
	

	
	
main()
