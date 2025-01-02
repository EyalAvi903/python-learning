import numpy as np

# Create a NumPy array of numbers from 1 to 10
numbers = np.arange(1, 11)  # Creates [1, 2, 3, ..., 10]

# Calculate the mean, sum, and product of the numbers
mean = np.mean(numbers)
total_sum = np.sum(numbers)
product = np.prod(numbers)

# Calculate the square of each number
squares = np.square(numbers)

# Print the results
print(f"Numbers: {numbers}")
print(f"Mean: {mean}")
print(f"Sum: {total_sum}")
print(f"Product: {product}")
print(f"Squares: {squares}")
