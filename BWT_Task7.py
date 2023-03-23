#Task-7: Functions in Python

#defining a funtion : docstrings : return value

def square(x):
	"""
	This is a doc string for this function. In this doc string
	we write about the functionality of this code, what arguments
	it expects and what it returns
	
	For example:
	
	Calculates the square of number
	Arguments:
		x: Any number
	Return Value: x^2
	"""
	return x**2;
	
print(square(3))


def sandwich(*components):
	print(components)

sandwich('chicken', 'ketchup', 'lettuce')
sandwich('turkey', 'thousand island')
sandwich('fish')
