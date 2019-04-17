#include <math.h>
#include <stdio.h>
#include "complex.h"
#include "mandelbrot.h"

int main() {

	printf("\nAndrew Oliveau	CS222	4/16/2019\n\n");
	double x, y;
	complex_t e; 

	for(x = -2.0; x <= 0.47; x += 0.06175) {
	
	e.r = x;
	
	for(y = -1.12; y <= 1.12; y += 0.077) {
		e.i = y;
		complex_t tmp = mandelbrot(e, 15);
		
		if(tmp.r == 10000) {
			printf(".");
		} else {
			printf(" ");
		}
	
	} 
	printf("\n");

	}
	return 1;
}