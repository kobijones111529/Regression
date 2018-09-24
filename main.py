import regression

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

data = GetData("data")

res = regression.LinearRegression(data)
print("a: {:.10f}\nb: {:.10f}".format(res[0], res[1]))
