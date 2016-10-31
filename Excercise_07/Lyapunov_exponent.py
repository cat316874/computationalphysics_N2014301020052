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
            temporary_omega = self.omega[i] + (-math.sin(midpoint_theta) - 0.6 * midpoint_omega + self.FD * math.sin(0.66666666667 * midpoint_time)) * self.dt
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
