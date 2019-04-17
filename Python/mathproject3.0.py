import math as m
f = lambda x: (54*(x**6) + 45*(x**5) - 102*(x**4) - 69*(x**3) + 35*(x**2) + 16*x - 4)

def quadratic(a, b, c):
    it = 0
    for r in range(7000):
        x0 = (a * f(b) * f(c)) / ((f(a) - f(b)) * (f(a) - f(c))) 
        x1 = (b * f(a) * f(c)) / ((f(b) - f(a)) * (f(b) - f(c)))
        x2 = (c * f(a) * f(b)) / ((f(c) - f(a)) * (f(c) - f(b)))
        x = x0 + x1 + x2
        if min(abs(x - a), abs(x - b), abs(x - c)) < 0.00001: 
            break
        a = b
        b = c
        c = x
        it += 1

    return c, it 

print(quadratic(0.1, 2, 0.5))





