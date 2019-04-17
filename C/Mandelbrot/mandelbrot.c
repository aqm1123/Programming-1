#include <math.h>
#include "complex.h"
#include "mandelbrot.h"


complex_t mandelbrot(complex_t c, int n) {

	complex_t c1;
	
	if(n > 0){
		
		c1 = mandelbrot(c, n-1);
		c1 = add_complex(multiply_complex(c1, c1), c);
	
	} else {
	
		return c;
	
	}			

	if (abs_complex(c1).r >= 10000){
		c1.i = 0;
		c1.r = 10000;
		return c1;
	} 

	return c1;
}