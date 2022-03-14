#plotting cost in logistic regression
from matplotlib import style
from matplotlib import pyplot as plt
import math
z=[-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0]
c=[]
def f(z):
    return (-(math.log(1/(1+math.exp(-z)))))
for a in z:
    k = f(a)
    c.append(k)
print(z)
print(c)
plt.plot(z,c)
plt.xlabel('z')
plt.ylabel('cost')
plt.show()