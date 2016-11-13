# Excercise_08

标签（空格分隔）： 计算物理

---
[TOC]

#Abstract
In this program I use the Runga-Kutta method to calculate the angle in phase with the frequency of the driving force after the transient period.Then I change the frequency for observation of the angle an find that the curves in the phase space are still similar. In the last part I plot the bifurcation diagram and a magnified version, and find the transition value of FD and calculate the first two value of the Feigenbaum delta in this system.

---
#Background
In last week's assignment we construct the chaos phenomenon by the method of phase space, this week we take the route to chaos by period doubling. As we change the strength of the driving force the periodic evolution of the angle doubles, so we can observe at certain points of the time. In this way, we can plot a bifurcation diagram and calculate the Feigenbaum constant.

---
#Main Text

##Poincare Section
The only difference between this task and the task of former week is that is this program we omit the transient period at the beginning of the evolution.
```python
class phase_diagram(physical_pendulum_v2):
    #Calculate the omega and theta in phase,omitting the transient period.
    def get_point_in_phase(self):
        for i in range(len(self.t)):
            if self.t[i] // (3 * math.pi) > 300:
                if ((2 / 3 * self.t[i]) % (2 * math.pi)) <= (2 / 3 * self.dt * 0.5) or (2 * math.pi - ((2 / 3 * self.t[i]) % (2 * math.pi))) <= (2 / 3 * self.dt * 0.5):
                    self.omega_in_phase.append(self.omega[i])
                    self.theta_in_phase.append(self.theta[i])
```
I use this `if` condition structure to omit the starting transient period.

The whole program are here.
```python
import math
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#Code for the using Latex in the tittle

class physical_pendulum_v2:
    '''docstring for assignment this week, using the Runga-Kutta method, with reseting process'''
    def __init__(self, FD, total_time, time_interval):
        self.FD = FD
        self.dt = time_interval
        self.steps = int(total_time // time_interval) + 1 #Should add an int() to convert the data type from float(possibly) to integer
        self.t = [0]
        self.omega = [0]
        self.theta = [0.2]
        self.energy = [1.9144]
        self.omega_in_phase = []
        self.theta_in_phase = []
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

class phase_diagram(physical_pendulum_v2):
    #Calculate the omega and theta in phase,omitting the transient period.
    def get_point_in_phase(self):
        for i in range(len(self.t)):
            if self.t[i] // (3 * math.pi) > 300:
                if ((2 / 3 * self.t[i]) % (2 * math.pi)) <= (2 / 3 * self.dt * 0.5) or (2 * math.pi - ((2 / 3 * self.t[i]) % (2 * math.pi))) <= (2 / 3 * self.dt * 0.5):
                    self.omega_in_phase.append(self.omega[i])
                    self.theta_in_phase.append(self.theta[i])
    def plot_diagram(self, color):
        plt.scatter(self.theta_in_phase, self.omega_in_phase, alpha = 0.01, linewidth = 0, c = color, label ='$F_D$ = '+str(self.FD))
        plt.title(r'Poincar\'{e} section $\omega$ versus $\theta$, $F_D$ = '+str(self.FD))
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.xlabel(r"$\theta$ (radian)")
        plt.xlim(-4,4)
        plt.ylim(-3,3)
        plt.legend(loc = 'best')


p1 = phase_diagram(FD = 1.35, total_time = 4000, time_interval = 0.01)
p1.calculate()
p1.get_point_in_phase()
p1.plot_diagram('b')
plt.show()

p2 = phase_diagram(FD = 1.4, total_time = 4000, time_interval = 0.01)
p2.calculate()
p2.get_point_in_phase()
p2.plot_diagram('r')
plt.show()

p3 = phase_diagram(FD = 1.44, total_time = 4000, time_interval = 0.01)
p3.calculate()
p3.get_point_in_phase()
p3.plot_diagram('g')
plt.show()

p4 = phase_diagram(FD = 1.465, total_time = 4000, time_interval = 0.01)
p4.calculate()
p4.get_point_in_phase()
p4.plot_diagram('m')
plt.show()


class phase_diagram_different_frequency(phase_diagram):
    def __init__(self, FD, total_time, time_interval, frequency):
        self.FD = FD
        self.dt = time_interval
        self.steps = int(total_time // time_interval) + 1 #Should add an int() to convert the data type from float(possibly) to integer
        self.t = [0]
        self.omega = [0]
        self.theta = [0.2]
        self.energy = [1.9144]
        self.omega_in_phase = []
        self.theta_in_phase = []
        self.frequency = frequency
    def get_point_in_phase(self):
        for i in range(len(self.t)):
            if self.t[i] // (3 * math.pi) > 300:
                if ((self.frequency * self.t[i]) % (2 * math.pi)) <= (self.frequency * self.dt * 1) or (2 * math.pi - ((self.frequency * self.t[i]) % (2 * math.pi))) <= (self.frequency * self.dt * 1):
                    self.omega_in_phase.append(self.omega[i])
                    self.theta_in_phase.append(self.theta[i])
    def plot_diagram(self, color):
        plt.scatter(self.theta_in_phase, self.omega_in_phase, alpha = 1, linewidth = 0, c = color, label ='$F_D$ = '+str(self.FD))
        plt.title(r'Poincar\'{e} section $\omega$ versus $\theta$')
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.xlabel(r"$\theta$ (radian)")
        plt.xlim(-4,4)
        plt.ylim(-3,3)
        plt.legend(loc = 'best')

p5 = phase_diagram_different_frequency(FD = 1.35, total_time = 4000, time_interval = 0.01, frequency = 1 / math.pi)
p5.calculate()
p5.get_point_in_phase()
p5.plot_diagram('b')
plt.show()

p6 = phase_diagram_different_frequency(FD = 1.4, total_time = 4000, time_interval = 0.01, frequency = 1 / math.pi)
p6.calculate()
p6.get_point_in_phase()
p6.plot_diagram('r')
plt.show()

p7 = phase_diagram_different_frequency(FD = 1.44, total_time = 4000, time_interval = 0.01, frequency = 1 / math.pi)
p7.calculate()
p7.get_point_in_phase()
p7.plot_diagram('g')
plt.show()

p8 = phase_diagram_different_frequency(FD = 1.465, total_time = 4000, time_interval = 0.01, frequency = 1 / math.pi)
p8.calculate()
p8.get_point_in_phase()
p8.plot_diagram('m')
plt.show()

p9 = phase_diagram_different_frequency(FD = 1.35, total_time = 4000, time_interval = 0.01, frequency = 1 / math.e)
p9.calculate()
p9.get_point_in_phase()
p9.plot_diagram('b')
plt.show()

p10 = phase_diagram_different_frequency(FD = 1.4, total_time = 4000, time_interval = 0.01, frequency = 1 / math.e)
p10.calculate()
p10.get_point_in_phase()
p10.plot_diagram('r')
plt.show()

p11 = phase_diagram_different_frequency(FD = 1.44, total_time = 4000, time_interval = 0.01, frequency = 1 / math.e)
p11.calculate()
p11.get_point_in_phase()
p11.plot_diagram('g')
plt.show()

p12 = phase_diagram_different_frequency(FD = 1.465, total_time = 4000, time_interval = 0.01, frequency = 1 / math.e)
p12.calculate()
p12.get_point_in_phase()
p12.plot_diagram('m')
plt.show()

p13 = phase_diagram_different_frequency(FD = 1.35, total_time = 4000, time_interval = 0.01, frequency = 1 / math.log(15))
p13.calculate()
p13.get_point_in_phase()
p13.plot_diagram('b')
plt.show()

p14 = phase_diagram_different_frequency(FD = 1.4, total_time = 4000, time_interval = 0.01, frequency = 1 / math.log(15))
p14.calculate()
p14.get_point_in_phase()
p14.plot_diagram('r')
plt.show()

p15 = phase_diagram_different_frequency(FD = 1.44, total_time = 4000, time_interval = 0.01, frequency = 1 / math.log(15))
p15.calculate()
p15.get_point_in_phase()
p15.plot_diagram('g')
plt.show()

p16 = phase_diagram_different_frequency(FD = 1.465, total_time = 4000, time_interval = 0.01, frequency = 1 / math.log(15))
p16.calculate()
p16.get_point_in_phase()
p16.plot_diagram('m')
plt.show()

p17 = phase_diagram_different_frequency(FD = 1.35, total_time = 4000, time_interval = 0.01, frequency = 3 / 5)
p17.calculate()
p17.get_point_in_phase()
p17.plot_diagram('b')
plt.show()

p18 = phase_diagram_different_frequency(FD = 1.4, total_time = 4000, time_interval = 0.01, frequency = 3 / 5)
p18.calculate()
p18.get_point_in_phase()
p18.plot_diagram('r')
plt.show()

p19 = phase_diagram_different_frequency(FD = 1.44, total_time = 4000, time_interval = 0.01, frequency = 3 / 5)
p19.calculate()
p19.get_point_in_phase()
p19.plot_diagram('g')
plt.show()

p20 = phase_diagram_different_frequency(FD = 1.465, total_time = 4000, time_interval = 0.01, frequency = 3 / 5)
p20.calculate()
p20.get_point_in_phase()
p20.plot_diagram('m')
plt.show()
```
In the second part of this program I change the original frequency to other ones that are irrational to the original one.
![e1](http://latex.codecogs.com/gif.latex?%7B%5COmega%7D_D%5Crightarrow%20%7B%7B%5COmega%7D_D%7D%27%3D1/e%2C1/%5Cpi%2C1/log%2815%29%2C3/5)
![1](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/FD_1_35.png)
![2](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/FD_1_4.png)
![3](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/FD_1_44.png)
![4](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/FD_1_465.png)
![5](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_pi_1.png)
![6](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_pi_2.png)
![7](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_pi_3.png)
![8](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_pi_4.png)
![9](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_e_1.png)
![10](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_e_2.png)
![11](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_e_3.png)
![12](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_e_4.png)
![13](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_log15_1.png)
![14](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_log15_2.png)
![15](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_log15_3.png)
![16](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_1_over_log15_4.png)
![17](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_3_over_5_1.png)
![18](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_3_over_5_2.png)
![19](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_3_over_5_3.png)
![20](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/frequency_3_over_5_4.png)

+ We do see that in the phase space the point is increasing from 1 to 4 as the driving force strength increases.
+ After I change the frequency to certain irrational ones we see that the curves in the phase space of __different frequencies__ do __resemble__! This is quite amazing!

##Bifurcation Diagram and the Feigenbaum Constant
In the last task we've seen that the number and the value of the points in the phase space are different for different value of the driving force strength. So in this program we plot the diagram for driving force strength versus angle.

I used an `loop` structure to calculate the value for different driving force strength.

```python
import math
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#Code for the using Latex in the tittle

class bifurcation_diagram_magnified:
    '''docstring for assignment this week, using the Runga-Kutta method, with reseting process'''
    def __init__(self, total_time, time_interval,driving_force_interval):
        self.FD = [1.35]
        self.dFD = driving_force_interval
        self.dt = time_interval
        self.steps = int(total_time // time_interval) + 1 #Should add an int() to convert the data type from float(possibly) to integer
        self.t = [0]
        self.omega = [0]
        self.theta = [0.2]
        self.theta_in_phase = []
        self.theta_fixed = []
        #Based on different driving_force_interval, we should build a corresponding array.
        while self.FD[-1] < 1.5:
            self.FD.append(self.FD[-1] + self.dFD)
    def calculate(self):
        for j in range(len(self.FD)):
            self.t = [0]
            self.omega = [0]
            self.theta = [0.2]
            self.omega_in_phase = []
            self.theta_in_phase = []
            for i in range(self.steps):
                midpoint_omega = self.omega[i] + 0.5 * (-math.sin(self.theta[i]) - 0.5 * self.omega[i] + self.FD[j] * math.sin(0.66666666667 * self.t[i])) * self.dt
                midpoint_time = self.t[i] + 0.5 * self.dt
                midpoint_theta = self.theta[i] + 0.5 * self.dt
                temporary_theta = self.theta[i] + midpoint_omega * self.dt
                temporary_omega = self.omega[i] + (-math.sin(midpoint_theta) - 0.5 * midpoint_omega + self.FD[j] * math.sin(0.66666666667 * midpoint_time)) * self.dt
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
            for i in range(len(self.t)):
                if self.t[i] // (3 * math.pi) > 300:
                    if ((2 / 3 * self.t[i]) % (2 * math.pi)) <= (2 / 3 * self.dt * 0.5) or (2 * math.pi - ((2 / 3 * self.t[i]) % (2 * math.pi))) <= (2 / 3 * self.dt * 0.5):
                        self.theta_in_phase.append(self.theta[i])
            plt.plot([self.FD[j]] * len(self.theta_in_phase), self.theta_in_phase,'b.', linewidth = 0, alpha = 0.1)
            #Note that in python, set a = [1, 2, 3], b = a[3] * 3 does not represents [3, 3, 3],it equals to 9!
            #If you want to construct [3, 3, 3], set b = [a[3]] * 3!
            #similarly, here I want to construct an array consisting of self.FD[j], and the number of self.FD[j] is len(self.theta_in_phase)
            plt.xlim(1.35, 1.5)
            plt.ylim(0.5, 3.5)
            plt.xlabel("$F_D$")
            plt.ylabel(r'$\theta$(radians)')
            plt.title(r'Bifurcation diagram $\theta$ versus $F_D$')
        plt.show()

a1 = bifurcation_diagram(total_time = 4000, time_interval = 0.01, driving_force_interval = 0.001)
a1.calculate()
```
Here are the outcomes:

![21](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/Bifurcation_diagram_original_frequency.png)
![22](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/Bifurcation_diagram_magnified.png)
![23](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/F1.png)
![24](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/F2.png)
![25](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/F3.png)
![26](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/F4.png)

+ We can see that my plot is exactly the same as the plot in the text book.
+ The four plots shows the first four value of the transformation point:
![27](http://latex.codecogs.com/gif.latex?F_1%3D1.4218%20%5Cquad%20F_2%3D1.4567%20%5Cquad%20F_3%3D1.4737%20%5Cquad%20F_4%3D1.4757%20%5Cquad%20%5C%5C%20%7B%5Cdelta%7D_n%3D%5Cfrac%7BF_n-F_%7Bn-1%7D%7D%7BF_%7Bn&plus;1%7D-F_n%7D%5Crightarrow%20%7B%5Cdelta%7D_1%3D2.917%5Cquad%20%7B%5Cdelta%7D_2%3D8.500)
+ However the calculated result is absurdly far from the known constant, this means that my calculation is not accurate enough.
+ Higher value of the transformation point is hard to get through the phase diagram and the bifurcation diagram, we still need to find a better way to get the value.

---
#Beyond the assignment
![28](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/Mandelbrot_zoom.gif)
Self similarity in the Mandelbrot set shown by zooming in on a round feature while panning in the negative-x direction. The display center pans from (−1, 0) to (−1.31, 0) while the view magnifies from 0.5 × 0.5 to 0.12 × 0.12 to approximate the Feigenbaum ratio
![29](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_08/Diagram_bifurkacji_anim_small.gif)

---
#Acknowledgement
+ Thanks author for providing a systematic guidence.
+ Thanks for the Wikipedia for the reference and the two gif.

