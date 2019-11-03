import matplotlib.pyplot as plt


theta0 = 1
theta1 = 0.5
x = [1,2,3,4,5]
arr = []

if __name__ == "__main__":
	# print(ans)
	for n in x:
		arr.append(theta0 + (theta1 * n))

	plt.plot(x,arr)
	plt.show()