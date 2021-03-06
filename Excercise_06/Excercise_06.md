﻿# Excercise_06

标签（空格分隔）： 计算物理

---
[TOC]

---

#Abstract
In this program I provide a numerical methods(Euler method) to solve the problem in page 31 and problem 2.9 in a wind-drag version and give some discriptive words to my program, in which I use the `class` to create my own new object and use the methods of this `class` to solve the problem.

---
#Background
When calculating the pojectory of the motion of a cannon shell, we usually only take the gravitation in account.This series of problem add the drag of air term,the adiabatic correction term and a changing g correction step by step to get close to the real projectory of the projectile motion of the cannon shell. Also in this problem the height of the target can change.So my aim is to find the angle with the maximum distance.

---
#Main Text
```python
import pylab as pl
import math
tool_list = []
distance = []
height = float(input("What is the height of the target(in meter):"))

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
    def get_the_distance(self):
        if max(self.y) >= height:
            for i in range(self.steps):
                if self.y[i] > height:
                    tool_list.append(self.x[i])
            print(tool_list[-1])
            distance.append(tool_list[-1])
            

angle_30 = two_point_seven(angle = 30, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_30.calculate()
angle_30.get_the_distance()
tool_list = []

angle_40 = two_point_seven(angle = 40, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_40.calculate()
angle_40.get_the_distance()
tool_list = []

angle_50 = two_point_seven(angle = 50, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_50.calculate()
angle_50.get_the_distance()
tool_list = []

angle_60 = two_point_seven(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_60.calculate()
angle_60.get_the_distance()
tool_list = []

angle_70 = two_point_seven(angle = 70, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_70.calculate()
angle_70.get_the_distance()
tool_list = []

angle_80 = two_point_seven(angle = 80, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_80.calculate()
angle_80.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
distance = []

angle_40 = two_point_seven(angle = 40, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_40.calculate()
angle_40.get_the_distance()
tool_list = []

angle_41 = two_point_seven(angle = 41, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_41.calculate()
angle_41.get_the_distance()
tool_list = []

angle_42 = two_point_seven(angle = 42, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_42.calculate()
angle_42.get_the_distance()
tool_list = []

angle_43 = two_point_seven(angle = 43, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_43.calculate()
angle_43.get_the_distance()
tool_list = []

angle_44 = two_point_seven(angle = 44, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44.calculate()
angle_44.get_the_distance()
tool_list = []

angle_45 = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45.calculate()
angle_45.get_the_distance()
tool_list = []

angle_46 = two_point_seven(angle = 46, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_46.calculate()
angle_46.get_the_distance()
tool_list = []

angle_47 = two_point_seven(angle = 47, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_47.calculate()
angle_47.get_the_distance()
tool_list = []

angle_48 = two_point_seven(angle = 48, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_48.calculate()
angle_48.get_the_distance()
tool_list = []

angle_49 = two_point_seven(angle = 49, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_49.calculate()
angle_49.get_the_distance()
tool_list = []

angle_50 = two_point_seven(angle = 50, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_50.calculate()
angle_50.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
distance = []

angle_44 = two_point_seven(angle = 44, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44.calculate()
angle_44.get_the_distance()
tool_list = []

angle_44_1 = two_point_seven(angle = 44.1, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_1.calculate()
angle_44_1.get_the_distance()
tool_list = []

angle_44_2 = two_point_seven(angle = 44.2, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_2.calculate()
angle_44_2.get_the_distance()
tool_list = []

angle_44_3 = two_point_seven(angle = 44.3, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_3.calculate()
angle_44_3.get_the_distance()
tool_list = []

angle_44_4 = two_point_seven(angle = 44.4, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_4.calculate()
angle_44_4.get_the_distance()
tool_list = []

angle_44_5 = two_point_seven(angle = 44.5, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_5.calculate()
angle_44_5.get_the_distance()
tool_list = []

angle_44_6 = two_point_seven(angle = 44.6, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_6.calculate()
angle_44_6.get_the_distance()
tool_list = []

angle_44_7 = two_point_seven(angle = 44.7, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_7.calculate()
angle_44_7.get_the_distance()
tool_list = []

angle_44_8 = two_point_seven(angle = 44.8, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_8.calculate()
angle_44_8.get_the_distance()
tool_list = []

angle_44_9 = two_point_seven(angle = 44.9, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_9.calculate()
angle_44_9.get_the_distance()
tool_list = []

angle_45 = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45.calculate()
angle_45.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
distance = []

angle_45 = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45.calculate()
angle_45.get_the_distance()
tool_list = []

angle_45_1 = two_point_seven(angle = 45.1, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_1.calculate()
angle_45_1.get_the_distance()
tool_list = []

angle_45_2 = two_point_seven(angle = 45.2, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_2.calculate()
angle_45_2.get_the_distance()
tool_list = []

angle_45_3 = two_point_seven(angle = 45.3, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_3.calculate()
angle_45_3.get_the_distance()
tool_list = []

angle_45_4 = two_point_seven(angle = 45.4, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_4.calculate()
angle_45_4.get_the_distance()
tool_list = []

angle_45_5 = two_point_seven(angle = 45.5, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_5.calculate()
angle_45_5.get_the_distance()
tool_list = []

angle_45_6 = two_point_seven(angle = 45.6, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_6.calculate()
angle_45_6.get_the_distance()
tool_list = []

angle_45_7 = two_point_seven(angle = 45.7, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_7.calculate()
angle_45_7.get_the_distance()
tool_list = []

angle_45_8 = two_point_seven(angle = 45.8, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_8.calculate()
angle_45_8.get_the_distance()
tool_list = []

angle_45_9 = two_point_seven(angle = 45.9, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_9.calculate()
angle_45_9.get_the_distance()
tool_list = []

angle_46 = two_point_seven(angle = 46, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_46.calculate()
angle_46.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
```
The main part of the program is the same as the former excercise, because I only need to find the maxmimum distance.

So the iteration expression is:
<img src="http://latex.codecogs.com/gif.latex?$$x_{i+1}=x_i+v_{x,i}\Delta t\\
v_{x,i+1}=v_{x,i}\\
y_{i+1}=y_i+v_{y,i}\Delta t\\
v_{y,i+1}=v_{y,i}-g\Delta t$$" alt="" title="" />.
Also the same as the former excercise.
```python
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
    def get_the_distance(self):
        if max(self.y) >= height:
            for i in range(self.steps):
                if self.y[i] > height:
                    tool_list.append(self.x[i])
            print(tool_list[-1])
            distance.append(tool_list[-1])
```
This is the calculation part.

What is different from the former excercise is that I add a `get_the_distance` method to calculate the the `x` value of the curve of shot cannon at the height of the target. Through this way we don't need to bother to design a brand new program to solve this problem.
```python
    def get_the_distance(self):
        if max(self.y) >= height:
            for i in range(self.steps):
                if self.y[i] > height:
                    tool_list.append(self.x[i])
            print(tool_list[-1])
            distance.append(tool_list[-1])
```
So if we set the height of the target as 1000m, we can calculate the maximum distance and the corresponding angle in this way.
```python

angle_30 = two_point_seven(angle = 30, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_30.calculate()
angle_30.get_the_distance()
tool_list = []

angle_40 = two_point_seven(angle = 40, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_40.calculate()
angle_40.get_the_distance()
tool_list = []

angle_50 = two_point_seven(angle = 50, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_50.calculate()
angle_50.get_the_distance()
tool_list = []

angle_60 = two_point_seven(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_60.calculate()
angle_60.get_the_distance()
tool_list = []

angle_70 = two_point_seven(angle = 70, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_70.calculate()
angle_70.get_the_distance()
tool_list = []

angle_80 = two_point_seven(angle = 80, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_80.calculate()
angle_80.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
distance = []

angle_40 = two_point_seven(angle = 40, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_40.calculate()
angle_40.get_the_distance()
tool_list = []

angle_41 = two_point_seven(angle = 41, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_41.calculate()
angle_41.get_the_distance()
tool_list = []

angle_42 = two_point_seven(angle = 42, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_42.calculate()
angle_42.get_the_distance()
tool_list = []

angle_43 = two_point_seven(angle = 43, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_43.calculate()
angle_43.get_the_distance()
tool_list = []

angle_44 = two_point_seven(angle = 44, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44.calculate()
angle_44.get_the_distance()
tool_list = []

angle_45 = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45.calculate()
angle_45.get_the_distance()
tool_list = []

angle_46 = two_point_seven(angle = 46, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_46.calculate()
angle_46.get_the_distance()
tool_list = []

angle_47 = two_point_seven(angle = 47, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_47.calculate()
angle_47.get_the_distance()
tool_list = []

angle_48 = two_point_seven(angle = 48, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_48.calculate()
angle_48.get_the_distance()
tool_list = []

angle_49 = two_point_seven(angle = 49, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_49.calculate()
angle_49.get_the_distance()
tool_list = []

angle_50 = two_point_seven(angle = 50, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_50.calculate()
angle_50.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
distance = []

angle_44 = two_point_seven(angle = 44, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44.calculate()
angle_44.get_the_distance()
tool_list = []

angle_44_1 = two_point_seven(angle = 44.1, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_1.calculate()
angle_44_1.get_the_distance()
tool_list = []

angle_44_2 = two_point_seven(angle = 44.2, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_2.calculate()
angle_44_2.get_the_distance()
tool_list = []

angle_44_3 = two_point_seven(angle = 44.3, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_3.calculate()
angle_44_3.get_the_distance()
tool_list = []

angle_44_4 = two_point_seven(angle = 44.4, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_4.calculate()
angle_44_4.get_the_distance()
tool_list = []

angle_44_5 = two_point_seven(angle = 44.5, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_5.calculate()
angle_44_5.get_the_distance()
tool_list = []

angle_44_6 = two_point_seven(angle = 44.6, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_6.calculate()
angle_44_6.get_the_distance()
tool_list = []

angle_44_7 = two_point_seven(angle = 44.7, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_7.calculate()
angle_44_7.get_the_distance()
tool_list = []

angle_44_8 = two_point_seven(angle = 44.8, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_8.calculate()
angle_44_8.get_the_distance()
tool_list = []

angle_44_9 = two_point_seven(angle = 44.9, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_9.calculate()
angle_44_9.get_the_distance()
tool_list = []

angle_45 = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45.calculate()
angle_45.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
distance = []

angle_45 = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45.calculate()
angle_45.get_the_distance()
tool_list = []

angle_45_1 = two_point_seven(angle = 45.1, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_1.calculate()
angle_45_1.get_the_distance()
tool_list = []

angle_45_2 = two_point_seven(angle = 45.2, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_2.calculate()
angle_45_2.get_the_distance()
tool_list = []

angle_45_3 = two_point_seven(angle = 45.3, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_3.calculate()
angle_45_3.get_the_distance()
tool_list = []

angle_45_4 = two_point_seven(angle = 45.4, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_4.calculate()
angle_45_4.get_the_distance()
tool_list = []

angle_45_5 = two_point_seven(angle = 45.5, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_5.calculate()
angle_45_5.get_the_distance()
tool_list = []

angle_45_6 = two_point_seven(angle = 45.6, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_6.calculate()
angle_45_6.get_the_distance()
tool_list = []

angle_45_7 = two_point_seven(angle = 45.7, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_7.calculate()
angle_45_7.get_the_distance()
tool_list = []

angle_45_8 = two_point_seven(angle = 45.8, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_8.calculate()
angle_45_8.get_the_distance()
tool_list = []

angle_45_9 = two_point_seven(angle = 45.9, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_9.calculate()
angle_45_9.get_the_distance()
tool_list = []

angle_46 = two_point_seven(angle = 46, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_46.calculate()
angle_46.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
'''
First we search the maximum in a rough range:
```python
angle_30 = two_point_seven(angle = 30, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_30.calculate()
angle_30.get_the_distance()
tool_list = []

angle_40 = two_point_seven(angle = 40, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_40.calculate()
angle_40.get_the_distance()
tool_list = []

angle_50 = two_point_seven(angle = 50, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_50.calculate()
angle_50.get_the_distance()
tool_list = []

angle_60 = two_point_seven(angle = 60, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_60.calculate()
angle_60.get_the_distance()
tool_list = []

angle_70 = two_point_seven(angle = 70, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_70.calculate()
angle_70.get_the_distance()
tool_list = []

angle_80 = two_point_seven(angle = 80, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_80.calculate()
angle_80.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
```
![1](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_06/QQ%E6%88%AA%E5%9B%BE20161024003923.png)
Then we suppose that our aim lies in the the range (40,50) degrees.
```python
angle_40 = two_point_seven(angle = 40, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_40.calculate()
angle_40.get_the_distance()
tool_list = []

angle_41 = two_point_seven(angle = 41, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_41.calculate()
angle_41.get_the_distance()
tool_list = []

angle_42 = two_point_seven(angle = 42, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_42.calculate()
angle_42.get_the_distance()
tool_list = []

angle_43 = two_point_seven(angle = 43, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_43.calculate()
angle_43.get_the_distance()
tool_list = []

angle_44 = two_point_seven(angle = 44, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44.calculate()
angle_44.get_the_distance()
tool_list = []

angle_45 = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45.calculate()
angle_45.get_the_distance()
tool_list = []

angle_46 = two_point_seven(angle = 46, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_46.calculate()
angle_46.get_the_distance()
tool_list = []

angle_47 = two_point_seven(angle = 47, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_47.calculate()
angle_47.get_the_distance()
tool_list = []

angle_48 = two_point_seven(angle = 48, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_48.calculate()
angle_48.get_the_distance()
tool_list = []

angle_49 = two_point_seven(angle = 49, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_49.calculate()
angle_49.get_the_distance()
tool_list = []

angle_50 = two_point_seven(angle = 50, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_50.calculate()
angle_50.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
```
So we see that the aim is about 45 degrees.
![2](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_06/QQ%E6%88%AA%E5%9B%BE20161024004037.png)
```python
angle_44 = two_point_seven(angle = 44, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44.calculate()
angle_44.get_the_distance()
tool_list = []

angle_44_1 = two_point_seven(angle = 44.1, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_1.calculate()
angle_44_1.get_the_distance()
tool_list = []

angle_44_2 = two_point_seven(angle = 44.2, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_2.calculate()
angle_44_2.get_the_distance()
tool_list = []

angle_44_3 = two_point_seven(angle = 44.3, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_3.calculate()
angle_44_3.get_the_distance()
tool_list = []

angle_44_4 = two_point_seven(angle = 44.4, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_4.calculate()
angle_44_4.get_the_distance()
tool_list = []

angle_44_5 = two_point_seven(angle = 44.5, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_5.calculate()
angle_44_5.get_the_distance()
tool_list = []

angle_44_6 = two_point_seven(angle = 44.6, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_6.calculate()
angle_44_6.get_the_distance()
tool_list = []

angle_44_7 = two_point_seven(angle = 44.7, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_7.calculate()
angle_44_7.get_the_distance()
tool_list = []

angle_44_8 = two_point_seven(angle = 44.8, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_8.calculate()
angle_44_8.get_the_distance()
tool_list = []

angle_44_9 = two_point_seven(angle = 44.9, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_44_9.calculate()
angle_44_9.get_the_distance()
tool_list = []

angle_45 = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45.calculate()
angle_45.get_the_distance()
tool_list = []

print(distance)
print(distance.index(max(distance)))
distance = []

angle_45 = two_point_seven(angle = 45, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45.calculate()
angle_45.get_the_distance()
tool_list = []

angle_45_1 = two_point_seven(angle = 45.1, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_1.calculate()
angle_45_1.get_the_distance()
tool_list = []

angle_45_2 = two_point_seven(angle = 45.2, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_2.calculate()
angle_45_2.get_the_distance()
tool_list = []

angle_45_3 = two_point_seven(angle = 45.3, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_3.calculate()
angle_45_3.get_the_distance()
tool_list = []

angle_45_4 = two_point_seven(angle = 45.4, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_4.calculate()
angle_45_4.get_the_distance()
tool_list = []

angle_45_5 = two_point_seven(angle = 45.5, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_5.calculate()
angle_45_5.get_the_distance()
tool_list = []

angle_45_6 = two_point_seven(angle = 45.6, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_6.calculate()
angle_45_6.get_the_distance()
tool_list = []

angle_45_7 = two_point_seven(angle = 45.7, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_7.calculate()
angle_45_7.get_the_distance()
tool_list = []

angle_45_8 = two_point_seven(angle = 45.8, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_8.calculate()
angle_45_8.get_the_distance()
tool_list = []

angle_45_9 = two_point_seven(angle = 45.9, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_45_9.calculate()
angle_45_9.get_the_distance()
tool_list = []

angle_46 = two_point_seven(angle = 46, initial_velocity = 700, x = 0, y = 0, time_of_duration = 200, time_interval = 0.05)
angle_46.calculate()
angle_46.get_the_distance()
tool_list = []
```
What surprises us is that the aim is so close to 45 degrees and we need to calculate higher order to get accurate result.
![3](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_06/QQ%E6%88%AA%E5%9B%BE20161024004111.png)
![4](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_06/QQ%E6%88%AA%E5%9B%BE20161024004124.png)

---

#Conclusion
+ The basic idea of the calculation process is rather simple: first look for the maximum in a larger range of angle ,then narrow down the searching area by picking the angles between the largest two angle calculated.
+ The iteration process is rather laborous and dull, and I'm eager to know if there is __way to create objects with a series of names through iteration structure__. I think this is very possible and I will ask the teacher for further detail.
+ If the creation of objected through iteration structure is realizable then this program can be greatly reduced in size. Once you imput the target height then you can just get the angle corresponding to the maximum distance.

---
Thanks to the teacher's guidence in class, and thanks to the textbook for its systematic guidence.