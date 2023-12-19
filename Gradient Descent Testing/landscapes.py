import numpy as np
from matplotlib import pyplot as plt

# TODO: add type hints for all function outputs

class Landscape():
	def __init__(self, description: str, objective, gradient, minima: list, dimensions: int): # TODO: add type hints
		self.description = description
		self.objective = objective
		self.grad = gradient
		self.minima = minima
		self.dimensions = dimensions
	
	def __str__(self):
		return self.description

	def cost(coordinates: list):
		assert len(coordinates) == self.dimensions
		return self.objective(coordinates)

	def gradient(coordinates: list):
		assert len(coordinates) == self.dimensions
		return self.grad(coordinates)

if __name__ == '__main__':
	def bessel_func(x: float, y: float):
	# TODO: docstring
		mag = np.sqrt(x**2 + y**2)
		return -1.0 * np.sin(mag) / mag

	def bessel_gradient(x: float, y: float):
	# TODO: docstring
		mag = np.sqrt(x**2 + y**2)
		common_term = -1.0 * (np.cos(mag) * mag - np.sin(mag)) / (mag**3)
		return x * common_term, y * common_term

	bessel = Landscape('my version of a bessel function in two dimensions',
				bessel_func,
				bessel_gradient,
				[(0, 0)],
				2) # TODO: figure out how to get vim to display docstrings
