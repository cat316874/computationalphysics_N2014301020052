# Excercise_12

标签（空格分隔）： 计算物理

---

[TOC]

---
#Abstract
Numerical partial differential equations is the branch of numerical analysis that studies the numerical solution of partial differential equations (PDEs).

---
#Background
##Electric potential
+ An electric potential (also called the electric field potential or the electrostatic potential) is the amount of electric potential energy that a unitary point electric charge would have if located at any point in space, and is equal to the work done by an external agent in carrying a unit of positive charge from the arbitrarily chosen reference point (usually infinity) to that point without any acceleration.
+ According to theoretical electromagnetics, electric potential is a scalar quantity denoted by V, equal to the electric potential energy of any charged particle at any location (measured in joules) divided by the charge of that particle (measured in coulombs). By dividing out the charge on the particle a remainder is obtained that is a property of the electric field itself.

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_12/ampere.jpg)

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_12/big_thumb.jpg)

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_12/4th_Eigenfunction_of_the_2D_Simple_Harmonic_Oscillator_2nd_perspective_view.jpg)

##Partial differential equation
+ In mathematics, a partial differential equation (PDE) is a differential equation that contains unknown multivariable functions and their partial derivatives. (A special case are ordinary differential equations (ODEs), which deal with functions of a single variable and their derivatives.) PDEs are used to formulate problems involving functions of several variables, and are either solved by hand, or used to create a relevant computer model.

+ PDEs can be used to describe a wide variety of phenomena such as sound, heat, electrostatics, electrodynamics, fluid dynamics, elasticity, or quantum mechanics. These seemingly distinct physical phenomena can be formalised similarly in terms of PDEs. Just as ordinary differential equations often model one-dimensional dynamical systems, partial differential equations often model multidimensional systems. PDEs find their generalisation in stochastic partial differential equations.

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_12/Heat_eqn.gif)

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_12/Navier_Stokes_Laminar.svg.png)

---
#Main Text
+ First, we encounter the Laplace's equation here:
![](http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;^&space;2V}{\partial&space;x&space;^&space;2}&space;+&space;\frac{\partial&space;^&space;2V}{\partial&space;y&space;^&space;2}&space;+&space;\frac{\partial&space;^&space;2V}{\partial&space;z&space;^&space;2}&space;=&space;0.)
and we use the iteration method, then this equation changed to:
![](http://www.codecogs.com/eqnedit.php?latex=V(i,&space;j,&space;k)&space;=&space;\frac{1}{6}[V(i&space;+&space;1,&space;j,&space;k)&space;+&space;V(i&space;-&space;1,&space;j,&space;k)&space;+&space;V(i,&space;j&space;+&space;1,&space;k)\\&space;+&space;V(i,&space;j&space;-&space;1,&space;k)&space;+&space;V(i,&space;j,&space;k&space;+&space;1)&space;+&space;V(i,&space;j,&space;k&space;-&space;1)])

+ For two finite parallel plate carrying electric charge, the potential distribution is like this:
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_12/1.png)
Code here:
```python
# import packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
# physical constants
c=1
r=1
k=1000

class wave:
    """Gaussian Initial Condition, Fixed Boundary Condition"""
    def __init__(self,x0=0.3,x1=0.7,length=1,time=30,dt=0.01):
        self.x0=x0
        self.x1=x1
        self.length=length
        self.time=time
        self.dt=dt
        self.dx=c*dt/r
        self.i=int(length/self.dx)+1
        self.n=time/dt
        self.X=np.linspace(0,length,self.i,endpoint=True)
        self.Y0=np.exp(-k*(self.X-x0)**2)+np.exp(-k*(self.X-x1)**2)
        return None
    def calculate(self):
        self.Y=[self.Y0]
        Y1=np.linspace(0,0,self.i)
        for cycle1 in range(self.i-2):
            Y1[cycle1+1]=2*(1-r**2)*self.Y0[cycle1+1]-self.Y0[cycle1+1]+r**2*(self.Y0[cycle1+2]+self.Y0[cycle1])
        self.Y.append(Y1)
        while not len(self.Y) > (self.n+1):
            newY=np.linspace(0,0,self.i)
            for cycle2 in range(self.i-2):
                newY[cycle2+1]=2*(1-r**2)*self.Y[-1][cycle2+1]-self.Y[-2][cycle2+1]+r**2*(self.Y[-1][cycle2+2]+self.Y[-1][cycle2])
            self.Y.append(newY)
        return None
    def plot(self,i):
        plt.plot(self.X,self.Y[i])
        return 0
    def movie(self):
        # New figure with white background
        fig = plt.figure(figsize=(6,6), facecolor='white')
        # New axis over the whole figure, no frame and a 1:1 aspect ratio
        ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)
        line, = ax.plot([], [], lw=2)
        def init():
            line.set_data([], [])
            return line,
        def animate(i):
            x = self.X
            y = self.Y[i]
            line.set_data(list(x), list(y))
            return line,
        anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=3000, interval=30)
        plt.show()
        return 0

A=wave()
A.calculate()
#A.plot(0)
#print A.Y
#print type(A.Y[1])


# New figure with white background
fig = plt.figure(figsize=(6,6), facecolor='white')
# New axis over the whole figure, no frame and a 1:1 aspect ratio
ax = plt.axes(xlim=(0, 1), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)
def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = A.X
    y = A.Y[i]
    line.set_data(list(x), list(y))
    return line,
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=10)
plt.show()
anim1.save('demoanimation.gif', writer='imagemagick', fps=4)
```
+ In numerical linear algebra, the method of successive over-relaxation (SOR) is a variant of the Gauss–Seidel method for solving a linear system of equations, resulting in faster convergence. A similar method can be used for any slowly converging iterative process.
+ It was devised simultaneously by David M. Young, Jr. and by Stanley P. Frankel in 1950 for the purpose of automatically solving linear systems on digital computers. Over-relaxation methods had been used before the work of Young and Frankel. An example is the method of Lewis Fry Richardson, and the methods developed by R. V. Southwell. However, these methods were designed for computation by human calculators, and they required some expertise to ensure convergence to the solution which made them inapplicable for programming on digital computers. These aspects are discussed in the thesis of David M. Young, Jr.

```python

from numpy import *
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import time
'''
class Electric_Field
this class solves the potential euation of capacitor
where:
              V1: potential of the left plate
              V2: potential of the right palte
              n: size of one side
'''
class ELECTRIC_FIELD(object):
    def __init__(self, V1=1, V2=-1, V_boundary=0, n=30):
        self.V1=float(V1)
        self.V2=float(V2)
        self.V_boundary=float(V_boundary)
        self.n=int(n)
        self.s1, self.s3=int(n/3), int(n/3)
        self.s2, self.s4=int(self.n-2-2*self.s1), int(self.n-2*self.s3)
        self.V=[]
        for j in range(self.n):
            self.V.append([0.0]*self.n)
        for j in [0,self.n-1]:
            self.V[j]=[self.V_boundary]*self.n
        for j in range(self.s3,self.s3+self.s4):
            self.V[j][self.s1]=self.V1
            self.V[j][self.s1+self.s2+1]=self.V2
    def update_V_Jacobi(self):
        self.counter=0                         # use Jacobi method solve the potential
        while True:
            self.V_next=[]
            for j in range(self.n):
                self.V_next.append([0.0]*self.n)
            for j in range(self.n):
                for i in range(self.n):
                    self.V_next[j][i]=self.V[j][i]
            self.delta_V=0.
            for j in range(1,self.n-1):
                for i in range(1,self.n-1):
                    if (j in range(self.s3,self.s3+self.s4)) and (i in [self.s1,self.s1+self.s2+1]):
                        continue
                    self.V_next[j][i]=1./4.*(self.V[j-1][i]+self.V[j+1][i]+self.V[j][i-1]+self.V[j][i+1])
                    self.delta_V=self.delta_V+abs(self.V_next[j][i]-self.V[j][i])
            self.counter=self.counter+1
            for j in range(self.n):
                for i in range(self.n):
                    self.V[j][i]=self.V_next[j][i]
            if (self.delta_V < abs(self.V2-self.V1)*(1.0E-5)*self.n*self.n and self.counter >= 10):
                break
        print ('jacobi itertion length n=',self.n,'  ',self.counter,' times')
        return self.counter
    def update_V_Gauss(self):              # use Gauss-Seidel method solve the potential
        self.counter=0
        while True:
            self.delta_V=0.
            for j in range(1,self.n-1):
                for i in range(1,self.n-1):
                    if (j in range(self.s3,self.s3+self.s4)) and (i in [self.s1,self.s1+self.s2+1]):
                        continue
                    self.next_V=1./4.*(self.V[j-1][i]+self.V[j+1][i]+self.V[j][i-1]+self.V[j][i+1])
                    self.delta_V=self.delta_V+abs(self.next_V-self.V[j][i])
                    self.V[j][i]=self.next_V
            self.counter=self.counter+1
            if (self.delta_V < abs(self.V2-self.V1)*(1.0E-5)*self.n*self.n and self.counter >= 10):
                break
        print ('gauss itertion length n=',self.n,'  ',self.counter,' times')
        return self.counter
    def update_V_SOR(self):           # use SOR method solve the potential
        self.alpha=2./(1.+pi/self.n)
        self.counter=0
        while True:
            self.delta_V=0.
            for j in range(1,self.n-1):
                for i in range(1,self.n-1):
                    if (j in range(self.s3,self.s3+self.s4)) and (i in [self.s1,self.s1+self.s2+1]):
                        continue
                    self.next_V=1./4.*(self.V[j-1][i]+self.V[j+1][i]+self.V[j][i-1]+self.V[j][i+1])
                    self.V[j][i]=self.alpha*(self.next_V-self.V[j][i])+self.V[j][i]
                    self.delta_V=self.delta_V+abs(self.alpha*(self.next_V-self.V[j][i]))
            self.counter=self.counter+1
            if (self.delta_V < abs(self.V2-self.V1)*(1.0E-5)*self.n*self.n and self.counter >= 10):
                break
        print ('SOR itertion length n=',self.n,'  ',self.counter,' times')
        return self.counter
    def Ele_field(self,x1,x2,y1,y2):       # calculate the Electirc field
        self.dx=abs(x1-x2)/float(self.n-1)
        self.Ex=[]
        self.Ey=[]
        for j in range(self.n):
            self.Ex.append([0.0]*self.n)
            self.Ey.append([0.0]*self.n)
        for j in range(1,self.n-1,1):
            for i in range(1,self.n-1,1):
                self.Ex[j][i]=-(self.V[j][i+1]-self.V[j][i-1])/(2*self.dx)
                self.Ey[j][i]=-(self.V[j-1][i]-self.V[j+1][i])/(2*self.dx)
    def plot_3d(self,ax,x1,x2,y1,y2):       # give 3d plot the potential
        self.x=linspace(x1,x2,self.n)
        self.y=linspace(y2,y1,self.n)
        self.x,self.y=meshgrid(self.x,self.y)
        self.surf=ax.plot_surface(self.x,self.y,self.V, rstride=1, cstride=1, cmap=cm.coolwarm)
        ax.set_xlim(x1,x2)
        ax.set_ylim(y1,y2)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
        ax.set_xlabel('x (m)',fontsize=14)
        ax.set_ylabel('y (m)',fontsize=14)
        ax.set_zlabel('Electric potential (V)',fontsize=14)
        ax.set_title('Potential near capacitor',fontsize=18)
    def plot_2d(self,ax1,ax2,x1,x2,y1,y2):     # give 2d plot of potential and electric field
        self.x=linspace(x1,x2,self.n)
        self.y=linspace(y2,y1,self.n)
        self.x,self.y=meshgrid(self.x,self.y)

        cs=ax1.contour(self.x,self.y,self.V)
        plt.clabel(cs, inline=1, fontsize=10)
        ax1.set_title('Equipotential lines',fontsize=18)
        ax1.set_xlabel('x (m)',fontsize=14)
        ax1.set_ylabel('y (m)',fontsize=14)

        for j in range(1,self.n-1,1):
            for i in range(1,self.n-1,1):
                ax2.arrow(self.x[j][i],self.y[j][i],self.Ex[j][i]/40,self.Ey[j][i]/40,fc='k', ec='k')
        ax2.set_xlim(-1.,1.)
        ax2.set_ylim(-1.,1.)
        ax2.set_title('Electric field',fontsize=18)
        ax2.set_xlabel('x (m)',fontsize=14)
        ax2.set_ylabel('y (m)',fontsize=14)
    def export_data(self,x1,x2,y1,y2):          # export data
        self.mfile=open(r'd:\data.txt','w')
        self.x=linspace(x1,x2,self.n)
        self.y=linspace(y2,y1,self.n)
        self.x,self.y=meshgrid(self.x,self.y)
        for j in range(self.n):
            for i in range(self.n):
                print >> self.mfile, self.x[j][i],self.y[j][i],self.V[j][i]
        self.mfile.close()

#  compare three method
n_min=10        # Jacobi method
n_max=50
n_jacobi=[]
iters_jacobi=[]
time_jacobi=[]
for i in range(n_min,n_max,2):
    start=time.clock()
    cmp=ELECTRIC_FIELD(1,-1,0,i)
    iters_jacobi.append(cmp.update_V_Jacobi())
    end=time.clock()

    time_jacobi.append(end-start)
    n_jacobi.append(i)


n_gauss=[]         # Gauss Seidel method
iters_gauss=[]
time_gauss=[]
for i in range(n_min,n_max,2):
    start=time.clock()
    cmp=ELECTRIC_FIELD(1,-1,0,i)
    iters_gauss.append(cmp.update_V_Gauss())
    end=time.clock()

    time_gauss.append(end-start)
    n_gauss.append(i)

n_SOR=[]       # SOR method
iters_SOR=[]
time_SOR=[]
for i in range(n_min,n_max,2):
    start=time.clock()
    cmp=ELECTRIC_FIELD(1,-1,0,i)
    iters_SOR.append(cmp.update_V_SOR())
    end=time.clock()
    time_SOR.append(end-start)
    n_SOR.append(i)
print (time_SOR)

#  export data
mfile=open(r'd:\initial_capacitor_26.txt','w')
for i in range(len(n_jacobi)):
    print >> mfile, n_jacobi[i], time_jacobi[i], time_gauss[i], time_SOR[i]
mfile.close()


# give a simple plot
fig=plt.figure(figsize=(14,7))
ax1=plt.axes([0.1,0.1,0.35,0.8])
ax2=plt.axes([0.55,0.1,0.35,0.8])

ax1.plot(n_jacobi,iters_jacobi,'or',markersize=5)
ax1.plot(n_gauss,iters_gauss,'ob',markersize=5)
ax1.plot(n_SOR,iters_SOR,'oy',markersize=5)
ax2.plot(n_jacobi,time_jacobi,'or',markersize=5)
ax2.plot(n_gauss,time_gauss,'ob',markersize=5)
ax2.plot(n_SOR,time_SOR,'oy',markersize=5)

plt.show(fig
```
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_12/iteration%20and%20time.png)

---
#Acknowledgement
+ Thanks to the auther for a systematically guidance
+ Thanks to Shixing Wang and Shijie Liu.
+ Thanks to the internet for provide pictures for the background.




