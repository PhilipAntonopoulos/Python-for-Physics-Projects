def v1prime(m1, m2, v1, v2):
    vel = v1*((m1-m2)/(m1+m2)) + v2*((2*m2)/(m1+m2))
    return vel

def v2prime(m1, m2, v1, v2):
    vel = v2*((m2-m1)/(m1+m2)) + v1*((2*m1)/(m1+m2))
    return vel

def timecol(x01, x02, v1, v2):
    t = (x02-x01)/(v1+v2)
    if t > 0:
        return t
    else:
        return 'null'

def xcol(x01, v1, delt):
    x = x01 + v1*delt
    return x

def pos1b(x01, v1, t):
        x = x01 + v1*t
        return x

def pos2b(x02, v2, t):
        x = x02 - v2*t
        return x

def pos1a(xcol, v1pr, t):
        x = xcol - v1pr * (t)
        return x


def pos2a(xcol, v2pr, t):
        x = xcol + v2pr * (t)
        return x
    



x01 = -10
x02 = 10
v1 = 2
v2 = 3
m1 = 1
m2 = 2

t0 = timecol(-10,10,2,3)
xcol = xcol(-10,2,t0)
v1pr = v1prime(1,2,2,-3)
v2pr = v2prime(1,2,2,-3)
print(v1pr,v2pr)

import numpy as np
import matplotlib.pyplot as plt

#fig, ax1 = plt.subplot(nrows = 1, ncols = 1)

x1 = []
x2 = []
t = np.arange(0,t0+1,1)

for i in t:
    x1.append(pos1b(-10,2,i))
    x2.append(pos2b(10,3,i))

plt.plot(x1,t, color ='orange', label = 'ball 1')
plt.plot(x2,t, color = 'blue', label = 'ball 2')

x1a = []
x2a = []


ta = np.arange(t0,2*t0+1,1)
print(ta)

for i in t:
    x1a.append(pos1a(xcol,abs(v1pr),i))
    x2a.append(pos2a(xcol,abs(v2pr),i))

plt.plot(x1a,ta, color = 'orange')
plt.plot(x2a,ta, color = 'blue')

plt.title("Minkowski Diagramm of a 1D Elastic Collision")
plt.xlabel("x(m)")
plt.ylabel("time")
plt.legend()



plt.show()

#print(t0,xcol,x1,x2)