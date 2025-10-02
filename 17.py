import math
def f(x):
    result = 0  # Initialize the sum
    for i in range(0, 20, 2):  # Loop through even numbers from 0 to 18
        x = (x**i / math.factorial(i)) * (-1)**(i // 2)  # Calculate each term of the series
        result += x  # Add the term to the sum
    return result  
b = math.pi / 3  
print(f(b))  
c = math.cos(b)  # Calculate the cosine of b using the math library
print(c)  