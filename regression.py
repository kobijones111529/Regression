import random

def LinearRegression(data):
	r = 0.01
	a = random.randrange(-1, 1)
	b = random.randrange(-1, 1)
	for i in range(1000):
		error = 0
		ga = 0
		gb = 0
		for p in data:
			x = p[0]
			y = p[1]
			yp = a * x + b
			error += 0.5 * (yp - y) ** 2
			ga += (yp - y) * x
			gb += (yp - y)

		a -= r * ga
		b -= r * gb

	return [a, b]
