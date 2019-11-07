import matplotlib.pyplot as plt
import random


theta0 = random.uniform(-50,50)
theta1 = random.uniform(-50,50)
x = [2104,1416,1534,852,3205,1222]
y = [460,232,315,178,594,220]
arr = []
learning = 0.00000002

def update(t1,t2,input,output):
	sum1 = 0
	sum2 = 0
	for i,j in zip(input, output):
		sum1 = sum1 + ((t1 +(t2*i)) - j)
	temp0 = theta0-learning*1/len(input)*sum1
	# TODO: verify that these formulas are behaving correctly. Write unit tests. Plot cost function (x axis = no of iterations, y axis = cost)
	for i,j in zip(input, output):
		sum2 = sum2 + (((t1 +(t2*i)) - j)*i)
	temp1 = theta1 - learning * 1 / len(input) * sum2

	return temp0, temp1

if __name__ == "__main__":
	plt.axis([-50,3000,-50,600])
	plt.plot(x, y, marker='x', linestyle='None')
	for i in range(150):
		print(theta0,theta1)
		theta0, theta1 = update(theta0, theta1, x, y)
		arr.clear()
		for i in x:
			arr.append(theta0 + (theta1 * i))
		plt.plot(x, arr)
		plt.pause(0.8)

	print(theta0, theta1)
	plt.show()
	# theta values after 5 iterations: 21.564, 0.18. -35.51, 0.21. 3.78, 0.19. 21.54, 0.18. -36.15, 0.21