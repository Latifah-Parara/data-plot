import matplotlib.pyplot as plt


theta0 = 0
theta1 = 0.5
x = [1,2,3,4,5]
ans = [theta0+(theta1*x)]
# def hypothesis(x):
# 	ans = theta0+(theta1*x)
# 	print(ans)


if __name__ == "__main__":
	# print(ans)
	plt.plot(ans)
	plt.show()