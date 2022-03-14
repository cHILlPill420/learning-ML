import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#random input data generation for linear model to train on

observations = 1000

# target=f(x,y)=a*x+b*y+c :: here a,b= weights & c= bias 
#for data:
#size for nprandomuniform = no. of observation x no. of variables
xs = np.random.uniform(-10,10,(observations,1))
ys = np.random.uniform(-10,10,(observations,1))

#combining xs and ys into one matrix:inputs[1000][2]
inputs = np.column_stack((xs,ys))
#print(inputs.shape)

#creating target
#let target= 2x-3y+5+noise : noise = always lies in real data
noise = np.random.uniform(-1,1,(observations,1))
targets = 2 * xs - 3 * ys + 5 + noise
#print(targets.shape)

#plotting the graph
targets = targets.reshape(observations,)
fig =  plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot(xs,ys,targets)
ax.set_xlabel('xs')
ax.set_ylabel('ys')
ax.set_zlabel('targets')
ax.view_init(azim=100)
plt.show()
targets = targets.reshape(observations,1)

#y=wx+b
#initialize weights and biases
rfwb= 0.1 #range for weights and biases
weights = np.random.uniform(-rfwb,rfwb,(2,1))
biases = np.random.uniform(-rfwb,rfwb,1)
#print(weights,biases)

#learning rate
lr= 0.05

#training the model
for i in range(100):
    #calculating outputs=y=wx+b
    outputs = np.dot(inputs,weights)+biases
    #compare outputs to targets
    deltas = outputs - targets
    #print loss=L2- Norm loss = summation of (yi - ti)^2
    #division by 2 for elegant update rules from gradient descent
    #division by observations for loss/observations = mean loss
    loss = np.sum(deltas ** 2)/2/observations
    print(loss)
    deltas_scaled = deltas/observations
    #w and b adjust
    #wi+1= wi -eta(learning rate)summation of (corresponding inputs * deltas)
    weights = weights - lr * ( np.dot(inputs.T, deltas_scaled))
    #bi+1= bi- eta*summation of deltas
    biases = biases - lr * (np.sum(deltas_scaled))

print(weights,biases)
#target= 2x-3y+5+noise: weight = close to 2 and -3 and bias= close to 5

#ploting  output and target
plt.plot(outputs,targets)
plt.xlabel('outputs')
plt.ylabel('targets')
plt.show()
