# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:29:46 2016

@author: 田
"""

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
