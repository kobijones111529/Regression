import sys
import random
import math

def GetData(fileName):
	file = open(fileName, "r")
	data_str = file.read()
	file.close()

	data_arr = data_str.split("\n")
	#remove empty lines
	for str in data_arr:
		if str == "":
			data_arr.remove(str)

	#remove whitespace
	for str in data_arr:
		str.replace(" ", "")

	data = [[0 for i in range(2)] for j in range(len(data_arr))]
	for i in range(len(data_arr)):
		point_str = data_arr[i].split(",")
		data[i][0] = float(point_str[0])
		data[i][1] = float(point_str[1])

	return data

points = GetData("data")

a = random.randrange(-1, 1)
b = random.randrange(-1, 1)
r = 0.01

se = [0 for x in range(5)]

for i in range(1000):
	e = 0
	ga = 0
	gb = 0
	for p in points:
		x = p[0]
		y = p[1]
		yp = a * x + b
		e += (yp - y) ** 2 / float(2)
		ga += (yp - y) * x
		gb += (yp - y)

	a -= r * ga
	b -= r * gb

	if i is 0:
		for x in range(len(se)):
			se[x] = e
	else:
		for x in range(1, len(se)):
			se[len(se) - x] = se[len(se) - x - 1]

		se[0] = e

	ea = 0
	for i in se:
		ea += i

	ea /= float(len(se))

	print(" e: " + "{:.10f}".format(e))
	print("ea: " + "{:.10f}".format(ea))
	print("    a: " + (" " if a >= 0 else "") + "{:.10f}".format(a))
	print("    b: " + (" " if b >= 0 else "") + "{:.10f}".format(b))
