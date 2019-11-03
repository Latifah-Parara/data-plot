import matplotlib.pyplot as plt


theta0 = 2
theta1 = 0.203
x = [2104,1416,1534,852]
y = [460,232,315,178]
arr = []
learning = 0.02

def cost(thetaA,thetaB,input,output):
	for i,j in zip(input, output):
		sumSq =((thetaA +(thetaB*i)) - j)**2
	return 1/2*len(input)*sumSq

def gradientDescent():
	return

if __name__ == "__main__":
	print(cost(theta0,theta1,x,y))
	for i in x:
		arr.append(theta0 + (theta1 * i))


	plt.plot(x,y, marker='x', linestyle='None')
	plt.plot(x,arr)
	plt.show()