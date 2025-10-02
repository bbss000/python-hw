import numpy as np

sum = 0  

# Loop through all odd numbers from 1 to 20,000,000 (inclusive)
for i in range(1, 2 * 10**7 + 1, 2):
    a = 1 / i * (-1) ** (i // 2)  # Calculate each term of the series
    sum += a  # Add the term to the sum

print(sum)  
print(np.pi / 4)  # Print the value of pi divided by 4 for comparison