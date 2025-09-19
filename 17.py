import math
def f(x):
    a =0
    for i in range(0 ,20, 2):
        x = (x**i/math.factorial(i))* (-1)**(i//2)
        a+=x
    return a
b = math.pi / 3
print(f(b))
c = math.cos(b)
print(c)
import numpy as np