import os
import sys
import numpy as np

if len(sys.argv) != 3:
	print 'please input valid params\n'
	sys.exit(-1)

inputpath = sys.argv[1]
outputpath = sys.argv[2]

print 'input data path : ', inputpath
print 'output data path: ', outputpath

x = np.loadtxt(inputpath)
y = np.loadtxt(outputpath)

assert len(x) == len(y), 'The size of input and output must be same.'

theta0 = 0
theta1 = 0
datasize = len(x)
learningrate = 0.01
iterateTime = 100

for i in range(iterateTime) :
	J = 0
	for j in range(datasize) :
		J += pow((theta0 + theta1 * x[j] - y[j]),2)
	J = J / (2.0 * datasize)
	print theta0, theta1, J
	tmptheta0 = 0
	tmptheta1 = 0
	for j in range(datasize) :
		tmptheta0 += theta0 + theta1 * x[j] - y[j]
		tmptheta1 += (theta0 + theta1 * x[j] - y[j]) * x[j]

	theta0 = theta0 - learningrate * (1.0 / datasize) * tmptheta0
	theta1 = theta1 - learningrate * (1.0 / datasize) * tmptheta1

	#print theta0, theta1
