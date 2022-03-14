#normal distribution
import random
import statistics
import math
from matplotlib import pyplot as plt
a = []
b = []
g = []
d = [1,2,3,4,5,6,7,8,9,10]
h=[]
for c in range(0,100):
    a.append(random.randint(1,10))
mu = statistics.mean(a)
sd = statistics.stdev(a)
v = statistics.variance(a)
print(a)
print(mu,sd,v)
gd = (1/(sd*math.sqrt(math.pi*2)))
for f in d:
    e = f-mu
    gdi = math.exp(-(e**2)/2*v)
    g.append(gdi)
print(g)
for c in range(0,100):
    h.append(random.randint(1,10))

# for c2 in range(0,100):
#     a2.append(random.randint(1,10))
# mu2 = statistics.mean(a2)
# sd2 = statistics.stdev(a2)
# v2 = statistics.variance(a2)
# print(a2)
# print(mu2,sd2,v2)
# gd2 = (1/(sd*math.sqrt(math.pi*2)))
# for f in d:
#     e2 = f-mu2
#     gdi2 = math.exp(-(e2**2)/2*v2)
#     g2.append(gdi2)
# print(g2)

#g3=[]
#g3=g1*g2

# for i in range(1,11):
#     k = a.count(i)
#     b.append(k)
#print(b)
plt.plot(d,g)
#3dplot a,a2,and g3
plt.title('Normal Distribution')
plt.xlabel('no.')
plt.ylabel('gs')
plt.show()

plt.plot(a,h)
plt.title('contour plot of two features')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()

