# Excercise_10

标签（空格分隔）： 计算物理

---

[TOC]
---
#Abstract
In this program I plot the motion of a mass point subjected to a central field for several different forms of field and plot the procession of the perihelion of the Mercury.

---
#Background
##Bertrand's theorem
In classical mechanics, Bertrand's theorem states that among central force potentials with bound orbits, there are only two types of central force potentials with the property that all bound orbits are also closed orbits: an inverse-square central force such as the gravitational or electrostatic potential

---
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/13cbc1cf1dc0f97d6eab6b78cd9980a8fe0828b4)

---
and the radial harmonic oscillator potential
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/ae9563b1a3d60988b1d67d4919e1aa14862d2dec)

---
The theorem was discovered by and named for the French mathematician Joseph Bertrand.
##Kepler's laws of planetary motion
In astronomy, Kepler's laws of planetary motion are three scientific laws describing the motion of planets around the Sun.

+ The orbit of a planet is an ellipse with the Sun at one of the two foci.
+ A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time.
+ The square of the orbital period of a planet is proportional to the cube of the semi-major axis of its orbit.
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/Kepler_laws_diagram.svg.png)

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/kepler2.gif)


---
#Main text
##Central force -- inverse
For central force of the form:

---
![](http://latex.codecogs.com/gif.latex?F_G%3D%5Cfrac%7BGM_E%20M_S%7D%7Br%5E%7B%5Cbeta%7D%7D%2C%5Cbeta%3E1)

---
We can study their traits of motion using the Euler-Cromer method.

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/2_01.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/2_5.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/2_997.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/1_high_velocity.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/1_low_velocity.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/1_starfish.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/1_sun.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/3.png)

+ As we can see that the curves of the motion is bounded for beta < 3.
+ For beta =1, the curve exhibit a procession-like shape.

Code here:
```python
import math
import matplotlib.pyplot as plt

class central_force:
    def __init__(self, x0, y0, vx0, vy0, beta, time_interval, total_time):
        self.beta = beta
        self.steps = int(total_time // time_interval) + 1
        self.dt = time_interval
        self.t = [0]
        self.x = [x0]
        self.y = [y0]
        self.vx = [vx0]
        self.vy = [vy0]
    def calculate(self):
        for i in range(self.steps):
            r_temporary = math.sqrt(self.x[i] ** 2 + self.y[i] ** 2)
            vx_temporary = self.vx[i] - (4 * math.pi ** 2 * self.x[i]) / r_temporary ** (self.beta + 1) * self.dt
            vy_temporary = self.vy[i] - (4 * math.pi ** 2 * self.y[i]) / r_temporary ** (self.beta + 1) * self.dt
            x_temporary = self.x[i] + vx_temporary * self.dt
            y_temporary = self.y[i] + vy_temporary * self.dt
            self.t.append(self.t[i] + self.dt)
            self.vx.append(vx_temporary)
            self.vy.append(vy_temporary)
            self.x.append(x_temporary)
            self.y.append(y_temporary)

t1 = central_force(x0 = 1, y0 = 0, vx0 = 0, vy0 = 2 * math.pi - 0.5, time_interval = 0.01, total_time = 100, beta = 3)
t1.calculate()

plt.plot(t1.x, t1.y,'b.')
plt.axis('equal')
plt.title('beta = 3,v_{y0} = 2\pi')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
```

---
##Central force -- proportional
 For central force of the form:
 ![](http://latex.codecogs.com/gif.latex?F_G%20%3D%20kr%5E2)
 
 ---
 The motion of the planet is like two dimensional oscilator:
 
 ---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/prop_6.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/prop_20.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/prop_100.png)

---
+ We can see that the orbit of the motion in such central field is also closed

---
+ We can also change the k for different direction and the orbit is just the Lissajous curve.

![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/prop_1_2.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/prop_3_2.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/prop_3_5.png)

Code here:
```python
import math
import matplotlib.pyplot as plt

class central_force:
    def __init__(self, x0, y0, vx0, vy0, beta, time_interval, total_time):
        self.beta = beta
        self.steps = int(total_time // time_interval) + 1
        self.dt = time_interval
        self.t = [0]
        self.x = [x0]
        self.y = [y0]
        self.vx = [vx0]
        self.vy = [vy0]
    def calculate(self):
        for i in range(self.steps):
            r_temporary = math.sqrt(self.x[i] ** 2 + self.y[i] ** 2)
            vx_temporary = self.vx[i] - (4 * math.pi ** 2 * self.x[i]) / r_temporary ** (self.beta + 1) * self.dt
            vy_temporary = self.vy[i] - (4 * math.pi ** 2 * self.y[i]) / r_temporary ** (self.beta + 1) * self.dt
            x_temporary = self.x[i] + vx_temporary * self.dt
            y_temporary = self.y[i] + vy_temporary * self.dt
            self.t.append(self.t[i] + self.dt)
            self.vx.append(vx_temporary)
            self.vy.append(vy_temporary)
            self.x.append(x_temporary)
            self.y.append(y_temporary)

t1 = central_force(x0 = 1, y0 = 0, vx0 = 0, vy0 = 2 * math.pi - 0.5, time_interval = 0.01, total_time = 100, beta = 3)
t1.calculate()

plt.plot(t1.x, t1.y,'b.')
plt.axis('equal')
plt.title('beta = 3,v_{y0} = 2\pi')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
```

---
##Procesion
+ We can calculate the orbit of the procession for a certain alpha:

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/Mercury_orbit.png)

---
+ Then measure the velocity of the procession of the perihelion of Mercury:

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/procession_1.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/procession_2.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/procession_3.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_10/procession_4.png)

---

Code here:
```python
import math
import matplotlib.pyplot as plt

class central_force:
    def __init__(self, x0, y0, vx0, vy0, time_interval, total_time):
        self.steps = int(total_time // time_interval) + 1
        self.dt = time_interval
        self.t = [0]
        self.x = [x0]
        self.y = [y0]
        self.vx = [vx0]
        self.vy = [vy0]
        self.r = [0.47]
    def calculate(self):
        for i in range(self.steps):         
            vx_temporary = self.vx[i] - (4 * math.pi ** 2 * self.x[i]) / self.r[i] ** 3 * (1+ 0.002 / self.r[i] ** 2) * self.dt
            vy_temporary = self.vy[i] - (4 * math.pi ** 2 * self.y[i]) / self.r[i] ** 3 * (1+ 0.002 / self.r[i] ** 2) * self.dt
            x_temporary = self.x[i] + vx_temporary * self.dt
            y_temporary = self.y[i] + vy_temporary * self.dt
            r_temporary = math.sqrt(x_temporary ** 2 + y_temporary ** 2)
            self.t.append(self.t[i] + self.dt)
            self.vx.append(vx_temporary)
            self.vy.append(vy_temporary)
            self.x.append(x_temporary)
            self.y.append(y_temporary)
            self.r.append(r_temporary)

t1 = central_force(x0 = 0.47, y0 = 0, vx0 = 0, vy0 = -8.2, time_interval = 0.01, total_time = 30)
t1.calculate()

t_max = []
theta_max = []

for i in range(len(t1.r)-2):
    if t1.r[i+1] > t1.r[i] and t1.r[i+1] > t1.r[i+2]:
        theta_max.append(math.atan(t1.y[i+1] / t1.x[i+1]))
        t_max.append(t1.t[i+1])
"""
print(t_max)
print(theta_max)
"""
plt.plot(t_max, theta_max,'+',t_max, theta_max,'-')
plt.xlabel('time(year)')
plt.ylabel('angle(radian)')
plt.title('Orbit orientation versus time,alpha = 0.002')
```

---
#Acknowledgement
+ Thanks to the author's systematic guidence.
+ Thanks to Internet for providing the pics.




