# Excercise_07

标签（空格分隔）： 计算物理

---
[TOC]

#Abstract
In this program I first use three numerical methods -- Euler-Cromer, Runga-Kutta and Verlet method -- to calculate the angle and energy evolution of the physical pendulum and make some comparisons of the results of three methods.Then I plot the phase diagram of the pendulum motion using the results from Runga-Kutta method and Sketch the Poincare section. What's more, I study the evolution of the angle difference in the low and high drive and calculate their Lyapunov exponent.

---
#Background
We have learn the Euler-Cromer method in class but I'm not content that I only grasp one numerical method so I learn the other two methods by myself and compare the results of the two methods to the result of Euler-Cromer method.

If we combine the drive and dissipation with the gravity component and make no approximation, we can will meet the chaos phenomenon when there is a high driving force.The article follows the guidance and esxhibit a series of results of the chaos phenomenon.

---
#Main Text

##Euler-Cromer Method
Iteration expression:
![e1](http://latex.codecogs.com/gif.latex?%24%24%7B%5Comega%7D_%7Bi&plus;1%7D%3D%7B%5Comega%7D_%7Bi%7D&plus;%5B-%28g/l%29sin%7B%5Ctheta%7D_i-q%7B%5Comega%7D_i&plus;F_D%20sin%28%7B%5COmega%7D_Dt_i%29%5D%5CDelta%20t%24%24)
<img src="http://latex.codecogs.com/gif.latex?$${\omega}_{i+1}={\omega}_{i}+[-(g/l)sin{\theta}_i-q{\omega}_i+F_D sin({\Omega}_Dt_i)]\Delta t\\
{\theta}_{i+1}={\theta}_i + {\omega}_{i+1}\Delta t$$" alt="" title="" />

The Euler-Cromer method use the approximation that is locally of first order and of order zero globally. So the deviation from the accurate result may increase rapidly as the variable goes larger.

```
class physical_pendulum_v1:
    '''docstring for three_point_ten, using the Euler-Cromer method, with reseting theta process'''
    def __init__(self, FD, total_time, time_interval):
        self.FD = FD
        self.dt = time_interval
        self.steps = int(total_time // time_interval) + 1 #Should add an int() to convert the data type from float(possibly) to integer
        self.t = [0]
        self.omega = [0]
        self.theta = [0.2]
        self.energy = [1.9144]
    def calculate(self):
        for i in range(self.steps):
            temporary_omega = self.omega[i] + (-math.sin(self.theta[i]) - 0.5 * self.omega[i] + self.FD * math.sin(0.66666666667 * self.t[i])) * self.dt
            #Shall not use the bracket in a math expression,because it will make a new sequence,for example:[2+(2+2)]+2 is meaningless
            self.omega.append(temporary_omega)
            temporary_theta = self.theta[i] + self.omega[i + 1] * self.dt
            if math.fabs(temporary_theta) > math.pi :
                if temporary_theta > 0 :
                    while temporary_theta > math.pi : #Can't use "for" structure here
                        temporary_theta = temporary_theta - 2 * math.pi
                else :  #Can't use "elif" here
                    while temporary_theta < -math.pi :
                        temporary_theta = temporary_theta  + 2 * math.pi
            self.theta.append(temporary_theta)
            self.t.append(self.t[i] + self.dt)
            self.energy.append(0.5 * 9.8 ** 2 * (temporary_omega) ** 2 + 9.8 * 9.8 * (1 - math.cos(temporary_theta))) # m=1

class physical_pendulum_v1_point_5(physical_pendulum_v1):
    '''docstring for three_point_ten, using the Euler-Cromer method, without reseting theta process'''
    def calculate(self):
        for i in range(self.steps):
            temporary_omega = self.omega[i] + (-math.sin(self.theta[i]) - 0.5 * self.omega[i] + self.FD * math.sin(0.66666666667 * self.t[i])) * self.dt
            #Shall not use the bracket in a math expression,because it will make a new sequence,for example:[2+(2+2)]+2 is meaningless
            self.omega.append(temporary_omega)
            temporary_theta = self.theta[i] + self.omega[i + 1] * self.dt
            self.theta.append(temporary_theta)
            self.t.append(self.t[i] + self.dt)
            self.energy.append(0.5 * 9.8 ** 2 * (temporary_omega) ** 2 + 9.8 * 9.8 * (1 - math.cos(temporary_theta))) # m=1
```
In my program I provide two version of calculation process,first with resetting the angle to the range [-pi,pi] and then without the resetting process.

##Runga-Kutta Method
The Euler-Cromer method evaluate the next value using the former value, and bring the error of second order. The Runga-Kutta method annihilate this disadvantage through a more symetric way of evaluating the next value by the value of the midpoint.

<img src="http://latex.codecogs.com/gif.latex?$$\frac{d\omega}{dt}=f(\theta,t)\\
{\omega}_{i+1}={\omega}_i+f({{\theta}_i}',{{\omega}_i}',t')\\
{{\theta}_i}' = {\theta}_i+\frac{1}{2}{\omega}_i\Delta t\\
{t_1}'=t_i+\frac{1}{2}\Delta t\\
{\theta}_{i+1}={\theta}_i+{{\omega}_i}'\Delta t\\
{{\omega}_i}'={\omega}_i+\frac{1}{2}f({\theta}_i,t_i)\Delta t$$" alt="" title="" />

And here are my code for the calculation:
```python
class physical_pendulum_v2(physical_pendulum_v1):
    '''docstring for assignment this week, using the Runga-Kutta method, with reseting process'''
    def calculate(self):
        for i in range(self.steps):
            midpoint_omega = self.omega[i] + 0.5 * (-math.sin(self.theta[i]) - 0.5 * self.omega[i] + self.FD * math.sin(0.66666666667 * self.t[i])) * self.dt
            midpoint_time = self.t[i] + 0.5 * self.dt
            midpoint_theta = self.theta[i] + 0.5 * self.dt
            temporary_theta = self.theta[i] + midpoint_omega * self.dt
            temporary_omega = self.omega[i] + (-math.sin(midpoint_theta) - 0.5 * midpoint_omega + self.FD * math.sin(0.66666666667 * midpoint_time)) * self.dt
            #Be sure not to miss the corresponding parenthesis, this bad syntax will make the whole folloing program return with invalid syntax.
            #Also, this suggest me that when I occurs to invalid syntax but after several check I still don't find any error , I should shift my attention to the upper line to see if I fail to pair parenthesis there!
            #Be familiar with the debugging method of commenting out!(delete the line that return error)
            if math.fabs(temporary_theta) > math.pi :
                if temporary_theta > 0 :
                    while temporary_theta > math.pi : #Can't use "for" structure here
                        temporary_theta = temporary_theta - 2 * math.pi
                else :  #Can't use "elif" here
                    while temporary_theta < -math.pi :
                        temporary_theta = temporary_theta  + 2 * math.pi
            self.theta.append(temporary_theta)
            self.omega.append(temporary_omega)
            self.t.append(self.t[i] + self.dt)
            self.energy.append(0.5 * 9.8 ** 2 * (temporary_omega) ** 2 + 9.8 * 9.8 * (1 - math.cos(temporary_theta))) # m=1

class physical_pendulum_v2_point_5(physical_pendulum_v1):
    '''docstring for assignment this week, using the Runga-Kutta method, without reseting process'''
    def calculate(self):
        for i in range(self.steps):
            midpoint_omega = self.omega[i] + 0.5 * (-math.sin(self.theta[i]) - 0.5 * self.omega[i] + self.FD * math.sin(0.66666666667 * self.t[i])) * self.dt
            midpoint_time = self.t[i] + 0.5 * self.dt
            midpoint_theta = self.theta[i] + 0.5 * self.dt
            temporary_theta = self.theta[i] + midpoint_omega * self.dt
            temporary_omega = self.omega[i] + (-math.sin(midpoint_theta) - 0.5 * midpoint_omega + self.FD * math.sin(0.66666666667 * midpoint_time)) * self.dt
            #Be sure not to miss the corresponding parenthesis, this bad syntax will make the whole folloing program return with invalid syntax.
            #Also, this suggest me that when I occurs to invalid syntax but after several check I still don't find any error , I should shift my attention to the upper line to see if I fail to pair parenthesis there!
            #Be familiar with the debugging method of commenting out!(delete the line that return error)
            self.theta.append(temporary_theta)
            self.omega.append(temporary_omega)
            self.t.append(self.t[i] + self.dt)
            self.energy.append(0.5 * 9.8 ** 2 * (temporary_omega) ** 2 + 9.8 * 9.8 * (1 - math.cos(temporary_theta))) # m=1
```

I also provide two version for the convenience of plotting.

##Verlet method
<img src="http://latex.codecogs.com/gif.latex?$${y}_{i+1}=2y_i-y_{i-1}+\frac{d^2y}{(dt)^2}(\Delta t)^2\\
 v \approx (y_{i+1}-y_{i-1})/2\Delta t\\
 {\theta}_{i+2}=2{\theta}_{i+1}-{\theta}_i+f({\theta}_{i+1}.{\omega}_{i+1},t_{i+1})\cdot(\Delta t)^2\\
 {\omega}_{i+1}=({\theta}_{i+2}-{\theta}_{i})/2\Delta t\\
$$" alt="" title="" />

This is the expression of Verlet method, we can solve the last two equations and will get
<img src="http://latex.codecogs.com/gif.latex?$${\theta}_{i+2}=\{2{\theta}_{i+1}-{\theta}_i+[-(g/l)sin{\theta}_{i+1}+(q/2\Delta t){\theta}_i+F_Dsin({\Omega}_D t_{i+1})](\Delta t)^2\}/(1+q\Delta t/2)$$" alt="" title="" />

It seem that Verlet method use an approximation of __fourth order__, however Verlet method alone can not start a calculation iteration, we should use the Euler-Cromer method to get the second value of angle and angular velocity, this action bring the approximation of the seconf order and will spread through the whole calculation process, thus we actually only get an approximation of __second order__.

And here is my code for the calculation process:
```python
class physical_pendulum_v3(physical_pendulum_v1):
    '''docstring for assignment this week, using the Verlet method, with the reseting process'''
    def calculate(self):
        #Use Euler-Cromer method to calculate the first value of theta.
        omega_1_in_E_C_method = self.omega[0] + (-math.sin(self.theta[0]) - 0.5 * self.omega[0] +self.FD * math.sin(0.66666666667 * self.t[0])) * self.dt
        self.omega.append(omega_1_in_E_C_method)
        self.theta.append(self.theta[0] + omega_1_in_E_C_method * self.dt)
        self.t.append(self.t[0] + self.dt)
        self.t.append(self.t[1] + self.dt)
        theta_2 = 2 * self.theta[1] - self.theta[0] + (-math.sin(self.theta[1]) - 0.5 * self.omega[1] + self.FD * math.sin(0.66666666667 * self.t[1])) * (self.dt) ** 2
        self.theta.append(theta_2)
        #re-calculate the second value of angular velocity
        self.omega[1] = (theta_2 - self.theta[0]) / (2 * self.dt)
        #Q: If I take this angular velocity into the calculation of the the third value of angle, will I get a more accurate solution?
        for i in range(self.steps):
            temporary_theta = (2 * self.theta[i+2] - self.theta[i+1] + (-math.sin(self.theta[i+2]) + (0.5 / (2 * self.dt)) * self.theta[i+1] + self.FD * math.sin(0.66666666667 * self.t[i+2])) * (self.dt) ** 2) / (1 + (0.5 * self.dt / 2))
            #angle i+3
            #I have already calculated theta 0,1,2. Since the loop condition starts from 0, the iteration expression starts from 0+3
            temporary_omega = (temporary_theta - self.theta[i+1]) / (2 * self.dt) #angular velocity i+2
            if math.fabs(temporary_theta) > math.pi:
                if temporary_theta > 0 :
                    while temporary_theta > math.pi : #Can't use "for" structure here
                        temporary_theta = temporary_theta - 2 * math.pi
                else :  #Can't use "elif" here
                    while temporary_theta < -math.pi :
                        temporary_theta = temporary_theta  + 2 * math.pi
            self.theta.append(temporary_theta)
            self.omega.append(temporary_omega)
            self.t.append(self.t[i+2] + self.dt)
        self.theta.remove(self.theta[-1])
        self.t.remove(self.t[-1])
        for i in range(self.steps + 2):
            self.energy.append(0.5 * 9.8 ** 2 * (self.omega[i]) ** 2 + 9.8 * 9.8 * (1 - math.cos(self.theta[i])))
        self.energy.remove(self.energy[0])
        #I've already got the first value of the energy in the initialization, so I must delete the first element of this list to keep the length of the list the same with other lists.

class physical_pendulum_v3_point_5(physical_pendulum_v1):
    '''docstring for assignment this week, using the Verlet method, without the reseting process'''
    def calculate(self):
        #Use Euler-Cromer method to calculate the first value of theta.
        omega_1_in_E_C_method = self.omega[0] + (-math.sin(self.theta[0]) - 0.5 * self.omega[0] +self.FD * math.sin(0.66666666667 * self.t[0])) * self.dt
        self.omega.append(omega_1_in_E_C_method)
        self.theta.append(self.theta[0] + omega_1_in_E_C_method * self.dt)
        self.t.append(self.t[0] + self.dt)
        self.t.append(self.t[1] + self.dt)
        theta_2 = 2 * self.theta[1] - self.theta[0] + (-math.sin(self.theta[1]) - 0.5 * self.omega[1] + self.FD * math.sin(0.66666666667 * self.t[1])) * (self.dt) ** 2
        self.theta.append(theta_2)
        #re-calculate the second value of angular velocity
        self.omega[1] = (theta_2 - self.theta[0]) / (2 * self.dt)
        #Q: If I take this angular velocity into the calculation of the the third value of angle, will I get a more accurate solution?
        for i in range(self.steps):
            temporary_theta = (2 * self.theta[i+2] - self.theta[i+1] + (-math.sin(self.theta[i+2]) + (0.5 / (2 * self.dt)) * self.theta[i+1] + self.FD * math.sin(0.66666666667 * self.t[i+2])) * (self.dt) ** 2) / (1 + (0.5 * self.dt / 2))
            #angle i+3
            #I have already calculated theta 0,1,2. Since the loop condition starts from 0, the iteration expression starts from 0+3
            temporary_omega = (temporary_theta - self.theta[i+1]) / (2 * self.dt) #angular velocity i+2
            self.theta.append(temporary_theta)
            self.omega.append(temporary_omega)
            self.t.append(self.t[i+2] + self.dt)
        self.theta.remove(self.theta[-1])
        self.t.remove(self.t[-1])
        for i in range(self.steps + 2):
            self.energy.append(0.5 * 9.8 ** 2 * (self.omega[i]) ** 2 + 9.8 * 9.8 * (1 - math.cos(self.theta[i])))
        self.energy.remove(self.energy[0])
```

I also provide two versions for the convenience of calculation.

##Results analysis
###Euler-Cromer Method

Euler-Cromer with resetting process:
![1](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/Euler_Cromer_resetting.png)

Euler-Cromer without resetting process:
![2](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/Euler_Cromer_without_resetting.png)

This result is actually the same result as the result in the textbook.We can conclude that:

+ A pendulum without a drive gradully __stops__ to move as a result of the __dissipative force__ which constantly draw energy from the system.

+ In the low drive situation the pendulum will eventually move along the force and exhibits a __periodic motion__.

+ In high drive situation the pendulum moves in a __aperiodic__ way and the evolution is extremely sensible to the initial value.   

###Runge-Kutta Method
![3](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/Runga_Kutta.png)

+ These results are almost the same with the results from Euler-Cromer method, and I will make further comparison with other results.

###Verlet Method
![4](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/Verlet.png)

+ These results are almost the same with the results from Euler-Cromer method, and I will make further comparison with other results.

###Comparison of the three sets of results of the evolution of the angle
![5](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/no_drive.png)
![6](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/low_drive_1.png)
![7](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/low_drive_2.png)
![8](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/low_drive_3.png)
![9](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/high_drive_comparison_0.04.png)

+ When there is no drive, the differences between the shape of three curves are __obvious__. I can not explain why.

+ When the drive is low, the differences between the shape of three curves are __tiny__ and we can find that the results from Runga-Kutta method differs from other two sets of results more, and this can be accounted by the fact that the Runga-Kutta method use an approximation of fourth order locally but the other two of second order.

+ For a high drive situation, when the `t` is small the three curves overlaps to a good extend, but as the time goes longer the deviation become much more obvious that the three curve almost take three __entirely different path.__

+ This discovery drive me to plot two more plot in high drive situation with smaller time interval and we can see the results:

![10](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/high_drive_comparison_0.02.png)

![11](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/high_drive_comparison_0.01.png)

+ We can compare the three figure and find that by decreasing the time interval we do make the divergent-starting value of time smaller but the three plots are __entirely different__ in the latter part of the plot, this also shows the charateristics of the chaos phenomenon.

###Energy evolution
![12](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/energy_evolution_1.png)
![13](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/energy_evolution_2.png)
![14](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/energy_evolution_3.png)
![15](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/energy_evolution_4.png)
![16](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/energy_evolution_5.png)

+ First, we can see that without a drive, the energy of the system __goes to zero rapidly.__

+ When the drive is low, the total enery first evolve in a irregular way, then the evolution of the energy of the system exhibit in a __periodic__ way.

+ When the drive gradually increase, the evolution become __chaotic__ features some sudden __blowing up__ and __jumping down__.

###Phase diagrams and the Poincare section

Phase diagrams of the five situation,using the results of Runga-Kutta method:
![17](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/phase_diagram_1.png)
![18](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/phase_diagram_2.png)
![19](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/phase_diagram_3.png)
![20](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/phase_diagram_4.png)
![21](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/phase_diagram_5.png)

+ We can see that obviously there are __three types of diagrams__.

+ The first type is for the situation without a drive, there is __no overlapping section__ in the phase diagram, which indicate the motion will eventually __decay__ with time and the system is __unstable__.

+ The second type is for the low drive situation. The trace of point in the phase diagram moves in a __periodic__ way and __overlapping__ part is very distinct.What's more,the phase diagram is __symmetric__ somehow.

+ The third type is for the situation of a high drive. The curve of the phase diagram is __much more sophisticated__.There are some __trend__ of the curves and some distinct __spiral structures__ in the diagram.The overlapping part is not so obvious as the low drive situation.

![22](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/Poincare_section.png)

+ For every <img src="http://latex.codecogs.com/gif.latex?$2\pi n$" alt="" title="" /> there are two closest value of t, so I construct a condition structure to find the nearest ones and add them to a new list.

```python
for i in range(len(Poincare_section.t)):
    if ((2 / 3 * Poincare_section.t[i]) % (2 * math.pi)) <= (2 / 3 * Poincare_section.dt * 1) or (2 * math.pi - ((2 / 3 * Poincare_section.t[i]) % (2 * math.pi))) <= (2 / 3 * Poincare_section.dt * 1):
        omega_in_phase.append(Poincare_section.omega[i])
        theta_in_phase.append(Poincare_section.theta[i])
```

+ In this way I get the list of `omega_in_phase` list and `theta_in_phase` list for plotting.

+ Also, I find it convenience to use the `.scatter()` method to plot this Poincare section.

+ This plot highly resembles the plot in the textbook.

###Angle difference evolution

```python
import math
import matplotlib.pyplot as plt
import numpy as np

class physical_pendulum_changing_initial_angle:
    def __init__(self, FD, total_time, time_interval, angle):
        self.FD = FD
        self.dt = time_interval
        self.steps = int(total_time // time_interval) + 1 #Should add an int() to convert the data type from float(possibly) to integer
        self.t = [0]
        self.omega = [0]
        self.initial_theta = angle
        self.theta = [self.initial_theta]
        self.energy = [1.9144]
    def calculate(self):
        for i in range(self.steps):
            midpoint_omega = self.omega[i] + 0.5 * (-math.sin(self.theta[i]) - 0.5 * self.omega[i] + self.FD * math.sin(0.66666666667 * self.t[i])) * self.dt
            midpoint_time = self.t[i] + 0.5 * self.dt
            midpoint_theta = self.theta[i] + 0.5 * self.dt
            temporary_theta = self.theta[i] + midpoint_omega * self.dt
            temporary_omega = self.omega[i] + (-math.sin(midpoint_theta) - 0.5 * midpoint_omega + self.FD * math.sin(0.66666666667 * midpoint_time)) * self.dt
            #Be sure not to miss the corresponding parenthesis, this bad syntax will make the whole folloing program return with invalid syntax.
            #Also, this suggest me that when I occurs to invalid syntax but after several check I still don't find any error , I should shift my attention to the upper line to see if I fail to pair parenthesis there!
            #Be familiar with the debugging method of commenting out!(delete the line that return error)
            self.theta.append(temporary_theta)
            self.omega.append(temporary_omega)
            self.t.append(self.t[i] + self.dt)
            self.energy.append(0.5 * 9.8 ** 2 * (temporary_omega) ** 2 + 9.8 * 9.8 * (1 - math.cos(temporary_theta))) # m=1

class physical_pendulum_changing_initial_angle_2(physical_pendulum_changing_initial_angle):
    def calculate(self):
        for i in range(self.steps):
            midpoint_omega = self.omega[i] + 0.5 * (-math.sin(self.theta[i]) - 0.6 * self.omega[i] + self.FD * math.sin(0.66666666667 * self.t[i])) * self.dt
            midpoint_time = self.t[i] + 0.5 * self.dt
            midpoint_theta = self.theta[i] + 0.5 * self.dt
            temporary_theta = self.theta[i] + midpoint_omega * self.dt
            temporary_omega = self.omega[i] + (-math.sin(midpoint_theta) - 0.5 * midpoint_omega + self.FD * math.sin(0.66666666667 * midpoint_time)) * self.dt
            #Be sure not to miss the corresponding parenthesis, this bad syntax will make the whole folloing program return with invalid syntax.
            #Also, this suggest me that when I occurs to invalid syntax but after several check I still don't find any error , I should shift my attention to the upper line to see if I fail to pair parenthesis there!
            #Be familiar with the debugging method of commenting out!(delete the line that return error)
            self.theta.append(temporary_theta)
            self.omega.append(temporary_omega)
            self.t.append(self.t[i] + self.dt)
            self.energy.append(0.5 * 9.8 ** 2 * (temporary_omega) ** 2 + 9.8 * 9.8 * (1 - math.cos(temporary_theta))) # m=1

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

p1_low_drive = physical_pendulum_changing_initial_angle(FD = 0.5, total_time = 50, time_interval = 0.01, angle = 0.2)
p2_low_drive = physical_pendulum_changing_initial_angle(FD = 0.5, total_time = 50, time_interval = 0.01, angle = 0.201)

p1_low_drive.calculate()
p2_low_drive.calculate()

angle_difference_1 =[]

for i in range(len(p2_low_drive.theta)):
    angle_difference_1.append(math.log(math.fabs(p2_low_drive.theta[i] - p1_low_drive.theta[i])))

plt.plot(p1_low_drive.t, angle_difference_1)
plt.title((r'$\theta$ versus time $F_D =0.5$ $q=0.5$'))
plt.ylabel(r'$\Delta \theta$ (radian)')
plt.xlabel("time (s)")
plt.xlim(0, 50)
plt.show()

p1_high_drive = physical_pendulum_changing_initial_angle(FD = 1.2, total_time = 150, time_interval = 0.01, angle = 0.2)
p2_high_drive = physical_pendulum_changing_initial_angle(FD = 1.2, total_time = 150, time_interval = 0.01, angle = 0.201)

p1_high_drive.calculate()
p2_high_drive.calculate()

angle_difference_2 = []

for i in range(len(p1_high_drive.theta)):
    angle_difference_2.append(math.log(math.fabs(p2_high_drive.theta[i] - p1_high_drive.theta[i])))

plt.plot(p1_high_drive.t, angle_difference_2)
plt.title((r'$\theta$ versus time $F_D =1.2$ $q=0.5$'))
plt.ylabel(r'$\Delta \theta$ (radian)')
plt.xlabel("time (s)")
plt.xlim(0, 150)
plt.show()

#change the damping factor by adding 0.001

p1_low_drive_2 = physical_pendulum_changing_initial_angle_2(FD = 0.5, total_time = 50, time_interval = 0.01, angle = 0.2)
p2_low_drive_2 = physical_pendulum_changing_initial_angle_2(FD = 0.5, total_time = 50, time_interval = 0.01, angle = 0.201)

p1_low_drive_2.calculate()
p2_low_drive_2.calculate()

angle_difference_1_2 =[]

for i in range(len(p2_low_drive_2.theta)):
    angle_difference_1_2.append(math.log(math.fabs(p2_low_drive_2.theta[i] - p1_low_drive_2.theta[i])))

plt.plot(p1_low_drive_2.t, angle_difference_1_2)
plt.title((r'$\theta$ versus time $F_D =0.5$ $q=0.6$'))
plt.ylabel(r'$\Delta \theta$ (radian)')
plt.xlabel("time (s)")
plt.xlim(0, 50)
plt.show()

p1_high_drive_2 = physical_pendulum_changing_initial_angle_2(FD = 1.2, total_time = 150, time_interval = 0.01, angle = 0.2)
p2_high_drive_2 = physical_pendulum_changing_initial_angle_2(FD = 1.2, total_time = 150, time_interval = 0.01, angle = 0.201)

p1_high_drive_2.calculate()
p2_high_drive_2.calculate()

angle_difference_2_2 = []

for i in range(len(p1_high_drive_2.theta)):
    angle_difference_2_2.append(math.log(math.fabs(p2_high_drive_2.theta[i] - p1_high_drive_2.theta[i])))

plt.plot(p1_high_drive_2.t, angle_difference_2_2)
plt.title((r'$\theta$ versus time $F_D =1.2$ $q=0.6$'))
plt.ylabel(r'$\Delta \theta$ (radian)')
plt.xlabel("time (s)")
plt.xlim(0, 150)
plt.show()
```
![23](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/Lyapunov_low_drive.png)
![24](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/Lyapunov_high_drive.png)

+ The initial angle difference is only __0.001 in radians__ .

+ When in low drive situation, the angle difference will decrease __exponentially__ and there are some __repeated structure__ in the plot. The approximate __Lyapunov exponent is 0.25__.

+ When in high drive situation, the angle differnce will increase __exponentially__ but in a __irregular__ way. The approximate __Lyapunov exponent is 0.07__.

![25](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/Lyapunov_low_drive_changed_damping_factor.png)
![26](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_07/Lyapunov_high_drive_changed_damping_factor.png)

+ After I changed the damping factor to 0.6, I found that the shape of the curve does no change very much, so the two __Lyapunov exponent are approximately the same__.

---

#Acknowledgement

+ Thanks for the systematic guidance of the text book.
+ Thanks for the matplotlib for providing this powerful tool to make plot.








