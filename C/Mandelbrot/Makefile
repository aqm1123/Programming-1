
CC = gcc
CFLAGS = -c 

main.o: main.c
	$(CC) $(CFLAGS) main.c
complex.o: complex.c
	$(CC) $(CFLAGS) complex.c
mandelbrot.o: mandelbrot.c
	$(CC) $(CFLAGS) mandelbrot.c

makeit: main.o complex.o mandelbrot.o 
	$(CC) main.o complex.o mandelbrot.o -o run -lm

clean:
	rm -rf *.exe
	rm -rf *.o

