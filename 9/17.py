import math
def f(x):
    a =0
    for i in range(1 ,21, 2):
        x = (x**i/math.factorial(i))* (-1)**(i//2)
        a+=x
    return a
b = math.pi / 6
print(f(b))
c = math.sin(b)
print(c)
import numpy as np