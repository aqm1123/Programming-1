#include <math.h>
#include "complex.h"

complex_t add_complex(complex_t c1, complex_t c2) {
	
	complex_t complex_sum;
	complex_sum.r = c1.r + c2.r;
	complex_sum.i = c1.i + c2.i;
	return(complex_sum);
}

complex_t abs_complex(complex_t c) {
	
	complex_t complex_abs;
	complex_abs.r = sqrt(c.r * c.r + c.i * c.i);
	complex_abs.i = 0;

	return complex_abs;
}


complex_t multiply_complex(complex_t c1, complex_t c2) {

	complex_t comp;
	comp.r = (c1.r * c2.r) - (c1.i * c2.i);
	comp.i = (c1.r * c2.i) + (c1.i * c2.r);
	return comp;

}