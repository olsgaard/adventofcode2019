import numpy as np

def calculate_fuel(array):
	return np.floor(array / 3).astype(int) - 2

assert np.all(
    calculate_fuel(np.array([12, 14, 1969, 100756])) == np.array([2,2,654,33583]).astype(int)
    )

data = np.loadtxt('input.txt')
result = calculate_fuel(data).sum()

print(result)
