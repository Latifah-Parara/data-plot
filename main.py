import matplotlib.pyplot as plt


theta0 = 7
theta1 = 0.2033
x = [2104,1416,1534,852]
y = [460,232,315,178]
arr = []
learning = 0.000002

def update(t1,t2,input,output):
	sum1 = 0
	sum2 = 0
	for i,j in zip(input, output):
		sum1 = sum1 + ((t1 +(t2*i)) - j)
	temp0 = theta0-learning*1/len(input)*sum1

	for i,j in zip(input, output):
		sum2 = sum2 + (((t1 +(t2*i)) - j)*i)
	temp1 = theta1 - learning * 1 / len(input) * sum2

	return temp0, temp1

def gradientDescent():
	return

if __name__ == "__main__":

	for i in x:
		print(theta0,theta1)
		theta0, theta1 = update(theta0, theta1, x, y)
		arr.clear()
		for i in x:
			arr.append(theta0 + (theta1 * i))
		plt.plot(x, arr)
		plt.pause(0.5)

	print(theta0, theta1)
	plt.plot(x, y, marker='x', linestyle='None')
	plt.show()