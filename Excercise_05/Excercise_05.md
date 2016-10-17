# Excercise_05

标签（空格分隔）： 计算物理

---
[TOC]

---

#Abstract
In this program I provide a numerical methods(Euler method) to solve the problem in page 31 and problem 2.6-2.9 give some discriptive words to my program, in which I use the `class` to create my own new object and use the methods of this `class` to solve the problem.

---
#Background
When calculating the pojectory of the motion of a cannon shell, we usually only take the gravitation in account.This series of problem add the drag of air term,the adiabatic correction term and a changing g correction step by step to get close to the real projectory of the projectile motion of the cannon shell.
--- 
#Main Text
##2.6
```python
import pylab as pl
import math

class two_point_six:
    """docstring for "2.6". Programmed by Yuan Tian."""
    def __init__(self, angle, x, y, initial_velocity, time_of_duration, time_interval):
        self.angle = angle * math.pi / 180
        self.angle_in_degree = angle
        self.v = initial_velocity
        self.x = [x]
        self.y = [y]
        self.t = [0]
        self.v_x = [initial_velocity * math.cos(self.angle)]
        self.v_y = [initial_velocity * math.sin(self.angle)]
        self.time = time_of_duration
        self.dt = time_interval
        self.steps = int(time_of_duration // time_interval + 1)
        print('Initial velocity ->', initial_velocity)
        print('Angel ->', angle)
        print('Time interval ->', time_interval)
        print('Total time ->', time_of_duration)
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i]
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.x, self.y, label = self.angle_in_degree)
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x')
        pl.ylabel('y')
        pl.ylim(0, 50)
        pl.legend(loc = 'best')
        pl.show()

class diff_angle(two_point_six):
    def show_results(self, style):
        pl.plot(self.x, self.y, label = self.angle_in_degree)
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x')
        pl.ylabel('y')
        pl.ylim(0, 22)
        pl.xlim(0, 45)
        pl.legend(loc = 'best')
        #There is no a pl.show() command which makes it possible to print different plot in one canvas!


a = diff_angle(angle = 60, initial_velocity = 20, x = 0, y = 0, time_of_duration = 5, time_interval = 0.05)
a.calculate()
a.show_results('g')

b = diff_angle(angle = 15, initial_velocity = 20, x = 0, y = 0, time_of_duration = 5, time_interval = 0.05)
b.calculate()
b.show_results('y')

c = diff_angle(angle = 30, initial_velocity = 20, x = 0, y = 0, time_of_duration = 5, time_interval = 0.05)
c.calculate()
c.show_results('g')


d = diff_angle(angle = 45, initial_velocity = 20, x = 0, y = 0, time_of_duration = 5, time_interval = 0.05)
d.calculate()
d.show_results('m')

e = diff_angle(angle = 75, initial_velocity = 20, x = 0, y = 0, time_of_duration = 5, time_interval = 0.05)
e.calculate()
e.show_results('k')

pl.show()
#This pl.show() make sure that the following plot wll not be plotted in the same canvas with this plot.

class Comparison(two_point_six):
    def show_results(self):
        self.x_accurate = []
        self.y_accurate = []
        for i in range(self.steps):
            tmp_x = self.v * math.cos(self.angle) * self.t[i]
            tmp_y = self.v * math.sin(self.angle) * self.t[i] - 0.5 * 9.8 * (self.t[i]) ** 2
            self.x_accurate.append(tmp_x)
            self.y_accurate.append(tmp_y)
        pl.plot(self.x_accurate, self.y_accurate, '--', label = 'Accurate solution ' + str(self.angle_in_degree))
        pl.plot(self.x, self.y, '-', label = 'Numerical solution ' + str(self.angle_in_degree))
        pl.xlabel('x')
        pl.ylabel('y')
        pl.ylim(0, 22)
        pl.xlim(0, 45)
        pl.legend(loc = 'best')
        pl.show()

f = Comparison(angle = 60, initial_velocity = 20, x = 0, y = 0, time_of_duration = 5, time_interval = 0.05)
f.calculate()
f.show_results()

g = Comparison(angle = 30, initial_velocity = 20, x = 0, y = 0, time_of_duration = 5, time_interval = 0.05)
g.calculate()
g.show_results()

h = Comparison(angle = 45, initial_velocity = 20, x = 0, y = 0, time_of_duration = 5, time_interval = 0.05)
h.calculate()
h.show_results()

class diff_angle_1(two_point_six):
    def show_results(self, style):
        pl.plot(self.x, self.y, label = self.angle_in_degree)
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x')
        pl.ylabel('y')
        pl.ylim(0, 45)
        pl.xlim(0, 95)
        pl.legend(loc = 'best')

i = diff_angle_1(angle = 60, initial_velocity = 30, x = 0, y = 0, time_of_duration = 10, time_interval = 0.05)
i.calculate()
i.show_results('g')

j = diff_angle_1(angle = 15, initial_velocity = 30, x = 0, y = 0, time_of_duration = 10, time_interval = 0.05)
j.calculate()
j.show_results('y')

k = diff_angle_1(angle = 30, initial_velocity = 30, x = 0, y = 0, time_of_duration = 10, time_interval = 0.05)
k.calculate()
k.show_results('g')


l = diff_angle_1(angle = 45, initial_velocity = 30, x = 0, y = 0, time_of_duration = 10, time_interval = 0.05)
l.calculate()
l.show_results('m')

m = diff_angle_1(angle = 75, initial_velocity = 30, x = 0, y = 0, time_of_duration = 10, time_interval = 0.05)
m.calculate()
m.show_results('k')
```

In this program we haven't consider the air drag.Like the former assignment, I use the `class` feature to work out an object-oriented-programming program.
$$x_{i+1}=x_i+v_{x,i}\Delta t\\
v_{x,i+1}=v_{x,i}\\
y_{i+1}=y_i+v_{y,i}\Delta t\\
v_{y,i+1}=v_{y,i}-g\Delta t$$
```python
def __init__(self, angle, x, y, initial_velocity, time_of_duration, time_interval):
        self.angle = angle * math.pi / 180
        self.angle_in_degree = angle
        self.v = initial_velocity
        self.x = [x]
        self.y = [y]
        self.t = [0]
        self.v_x = [initial_velocity * math.cos(self.angle)]
        self.v_y = [initial_velocity * math.sin(self.angle)]
        self.time = time_of_duration
        self.dt = time_interval
        self.steps = int(time_of_duration // time_interval + 1)
        print('Initial velocity ->', initial_velocity)
        print('Angel ->', angle)
        print('Time interval ->', time_interval)
        print('Total time ->', time_of_duration)
```
This part is the initializer.
```python
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i]
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
```
The calculate method.

```python
def show_results(self):
        pl.plot(self.x, self.y, label = self.angle_in_degree)
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x')
        pl.ylabel('y')
        pl.ylim(0, 50)
        pl.legend(loc = 'best')
        pl.show()
```
Show_results method.

![01](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_05/01.jpg)
This plot shows the projectories of motions in different angle; we can see that the projectory with 45 degree reach the furthest.
![02](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_05/02.jpg)
![03](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_05/03.jpg)
![04](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_05/04.jpg)
This series of plot shows the comparison between the numerical results and the accurate results.They both share the feature that the accurate results are inside the numerical results.It's not hard to understand this since we use the Euler method to calculate.We will always get a point outside the curve through the approximatation.
![05](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_05/05.jpg)
This plot shows the projectories for a different initial velocity and for diferrent angle.This time the projectory in 45 degree also goes the furthest. 

##2.7&2.9
```python
import pylab as pl
import math

class two_point_six:
    """docstring for "2.6". Programmed by Yuan Tian."""
    def __init__(self, angle, x, y, initial_velocity, time_of_duration, time_interval):
        self.angle = angle * math.pi / 180
        self.angle_in_degree = angle
        self.v = initial_velocity
        self.V_i = [initial_velocity]
        self.x = [x]
        self.y = [y]
        self.t = [0]
        self.v_x = [initial_velocity * math.cos(self.angle)]
        self.v_y = [initial_velocity * math.sin(self.angle)]
        self.time = time_of_duration
        self.dt = time_interval
        self.steps = int(time_of_duration // time_interval + 1)
        print('Initial velocity ->', initial_velocity)
        print('Angel ->', angle)
        print('Time interval ->', time_interval)
        print('Total time ->', time_of_duration)
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i]
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
    def show_results(self, style):
        pl.plot(self.x, self.y, style,  label = 'Non-dragging model '+str(self.angle_in_degree))
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.ylim(0, 15000)
        pl.xlim(0, 25000)
        pl.legend(loc = 'best')


class two_point_seven(two_point_six):
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i] - ((1- 0.0065 * self.y[i] / 283) ** 2.5) * (0.00004 * self.V_i[i] * self.v_x[i] * self.dt)
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt -((1- 0.0065 * self.y[i] / 283) ** 2.5) * (0.00004 * self.V_i[i] * self.v_y[i] * self.dt)
            tmp_v_i = math.sqrt((self.v_x[i]) ** 2 + (self.v_y[i]) ** 2)
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
            self.V_i.append(tmp_v_i)
    def show_results(self, style):
        pl.plot(self.x, self.y, style,  label = 'Adiabatic model '+str(self.angle_in_degree))
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.ylim(0, 15000)
        pl.xlim(0, 25000)
        pl.legend(loc = 'best')

class without_adiabatic(two_point_six):
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i] - (0.00004 * self.V_i[i] * self.v_x[i] * self.dt)
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt - (0.00004 * self.V_i[i] * self.v_y[i] * self.dt)
            tmp_v_i = math.sqrt((self.v_x[i]) ** 2 + (self.v_y[i]) ** 2)
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
            self.V_i.append(tmp_v_i)
    def show_results(self, style):
        pl.plot(self.x, self.y, style,  label = 'Non-adiabatic model '+str(self.angle_in_degree))
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.ylim(0, 15000)
        pl.xlim(0, 25000)
        pl.legend(loc = 'best')

a = two_point_six(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
b = two_point_seven(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
c = without_adiabatic(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
a.calculate()
b.calculate()
c.calculate()
a.show_results('--')
b.show_results('-')
c.show_results('-.')
pl.show()

d = two_point_six(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
e = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
f = without_adiabatic(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
d.calculate()
e.calculate()
f.calculate()
d.show_results('--')
e.show_results('-')
f.show_results('-.')
```
```python
class two_point_seven(two_point_six):
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i] - ((1- 0.0065 * self.y[i] / 283) ** 2.5) * (0.00004 * self.V_i[i] * self.v_x[i] * self.dt)
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt -((1- 0.0065 * self.y[i] / 283) ** 2.5) * (0.00004 * self.V_i[i] * self.v_y[i] * self.dt)
            tmp_v_i = math.sqrt((self.v_x[i]) ** 2 + (self.v_y[i]) ** 2)
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
            self.V_i.append(tmp_v_i)
    def show_results(self, style):
        pl.plot(self.x, self.y, style,  label = 'Adiabatic model '+str(self.angle_in_degree))
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.ylim(0, 15000)
        pl.xlim(0, 25000)
        pl.legend(loc = 'best')
```
This is `class` created based on the former calculation to calculate the situation with an air drag and the adiabatic correction.I use the formula from the book:
$$\rho = {\rho}_0(1-\frac{ay}{T_0})^{\alpha} \\
F_{drag}^{*}=\frac{\rho}{{\rho}_0}F_{drag}(y=0)$$
```python
class without_adiabatic(two_point_six):
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i] - (0.00004 * self.V_i[i] * self.v_x[i] * self.dt)
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt - (0.00004 * self.V_i[i] * self.v_y[i] * self.dt)
            tmp_v_i = math.sqrt((self.v_x[i]) ** 2 + (self.v_y[i]) ** 2)
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
            self.V_i.append(tmp_v_i)
    def show_results(self, style):
        pl.plot(self.x, self.y, style,  label = 'Non-adiabatic model '+str(self.angle_in_degree))
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.ylim(0, 15000)
        pl.xlim(0, 25000)
        pl.legend(loc = 'best')
```
I also created a `class` to support the comparison between the projectories with and without adiabatic correction.
![06](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_05/06.jpg)
![07](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_05/07.jpg)
From these two plots we can see that in both angle the relative relation on the three projectories is the same.The projectory without air drag fly high into the sky;the projectory with density correction goes further than the projectory without density correction does.This result is consistant with the result in the text book.

##2.8
```python
import pylab as pl
import math

class two_point_six:
    """docstring for "2.6". Programmed by Yuan Tian."""
    def __init__(self, angle, x, y, initial_velocity, time_of_duration, time_interval):
        self.angle = angle * math.pi / 180
        self.angle_in_degree = angle
        self.v = initial_velocity
        self.V_i = [initial_velocity]
        self.x = [x]
        self.y = [y]
        self.t = [0]
        self.v_x = [initial_velocity * math.cos(self.angle)]
        self.v_y = [initial_velocity * math.sin(self.angle)]
        self.time = time_of_duration
        self.dt = time_interval
        self.steps = int(time_of_duration // time_interval + 1)
        print('Initial velocity ->', initial_velocity)
        print('Angel ->', angle)
        print('Time interval ->', time_interval)
        print('Total time ->', time_of_duration)
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i]
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
    def show_results(self, style):
        pl.plot(self.x, self.y, style,  label = 'Non-dragging model '+str(self.angle_in_degree))
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.ylim(0, 15000)
        pl.xlim(0, 25000)
        pl.legend(loc = 'best')


class two_point_seven(two_point_six):
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i] - ((1- 0.0065 * self.y[i] / 283) ** 2.5) * (0.00004 * self.V_i[i] * self.v_x[i] * self.dt)
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt -((1- 0.0065 * self.y[i] / 283) ** 2.5) * (0.00004 * self.V_i[i] * self.v_y[i] * self.dt)
            tmp_v_i = math.sqrt((self.v_x[i]) ** 2 + (self.v_y[i]) ** 2)
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
            self.V_i.append(tmp_v_i)
    def show_results(self, style):
        pl.plot(self.x, self.y, style,  label = 'Adiabatic model '+str(self.angle_in_degree))
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.ylim(0, 15000)
        pl.xlim(0, 25000)
        pl.legend(loc = 'best')

class without_adiabatic(two_point_six):
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i] - (0.00004 * self.V_i[i] * self.v_x[i] * self.dt)
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * self.dt - (0.00004 * self.V_i[i] * self.v_y[i] * self.dt)
            tmp_v_i = math.sqrt((self.v_x[i]) ** 2 + (self.v_y[i]) ** 2)
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
            self.V_i.append(tmp_v_i)
    def show_results(self, style):
        pl.plot(self.x, self.y, style,  label = 'Non-adiabatic model '+str(self.angle_in_degree))
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.ylim(0, 15000)
        pl.xlim(0, 25000)
        pl.legend(loc = 'best')

class changing_g(two_point_six):
    def calculate(self):
        for i in range(self.steps):
            tmp_x = self.x[i] + self.v_x[i] * self.dt
            tmp_v_x = self.v_x[i] - ((1- 0.0065 * self.y[i] / 283) ** 2.5) * (0.00004 * self.V_i[i] * self.v_x[i] * self.dt)
            tmp_y = self.y[i] + self.v_y[i] * self.dt
            tmp_v_y = self.v_y[i] - 9.8 * (6371000 / (6371000 + self.y[i]) ) ** 2 * self.dt -((1- 0.0065 * self.y[i] / 283) ** 2.5) * (0.00004 * self.V_i[i] * self.v_y[i] * self.dt)
            tmp_v_i = math.sqrt((self.v_x[i]) ** 2 + (self.v_y[i]) ** 2)
            self.x.append(tmp_x)
            self.y.append(tmp_y)
            self.v_x.append(tmp_v_x)
            self.v_y.append(tmp_v_y)
            self.t.append(self.t[i] + self.dt)
            self.V_i.append(tmp_v_i)
    def show_results(self, style):
        pl.plot(self.x, self.y, style,  label = 'Changing-g model '+str(self.angle_in_degree))
        pl.title('Trajectories of the cannon shell')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.ylim(0, 15000)
        pl.xlim(0, 25000)
        pl.legend(loc = 'best')

a = two_point_six(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
b = two_point_seven(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
c = without_adiabatic(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
d = changing_g(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
a.calculate()
b.calculate()
c.calculate()
d.calculate()
a.show_results('--')
b.show_results('-')
c.show_results('-.')
d.show_results('b')
pl.show()

d = two_point_six(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
e = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
f = without_adiabatic(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
g = changing_g(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
d.calculate()
e.calculate()
f.calculate()
g.calculate()
d.show_results('--')
e.show_results('-')
f.show_results('-.')
g.show_results('b')
```
In this program I creat a `class` based on former calculation to calculate the projectories with changing-g correction.
$$g(y_i)=g_0(\frac{R}{R+y_i})^2$$
The $R$ is the average radius of the earth and I derive this term from the gravitation fromula.
![08](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_05/08.jpg)
![09](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_05/09.jpg)
Compared to former plots, we can see that the projectories with and without a changing-g correction almost overlap each other, this means that even for a cannon shell shot with initial velocity of 700m/s this correction does not bring further obvious change to the calculation results thus it's unnecessary to bring into this correction.

---

#Conclution
+ The projectories with 45 degree will alway goes the furthest in a model without air dag no matter the value of the initial velocity.
+ Comparing to accurate results, the numerical results using the Euler method will always get a curve "outside" the accurate results, because the Euler method uses the linear approximation and thus will always get a point ouside the accurate result.
+ The projectories with no air drag goes significantly higher and further than the ones with air drag. The projectories with adiabatic correction goes a little bit further than the ones without correction.
+ The changing-g correction is unnecessary even for a cannon shell shot with high speed. Thus we don't need to bring in this correction.
+ Numerical calculation gives an intuative idea of how the corrections change the outcome and to what extent they change the outcome. This also help me to decide which correction is necessary and which is not.

---

#Acknowledgement
Thanks to the teacher's guidence in class, and thanks to the textbook for its systematic guidence.


