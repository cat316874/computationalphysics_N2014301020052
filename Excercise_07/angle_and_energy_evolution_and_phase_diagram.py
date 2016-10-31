import math
import matplotlib.pyplot as plt
import numpy as np

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

v1_1 = physical_pendulum_v1(FD = 0, total_time = 60, time_interval = 0.04)
v1_2 = physical_pendulum_v1(FD = 0.1, total_time = 60, time_interval = 0.04)
v1_3 = physical_pendulum_v1(FD = 0.5, total_time = 60, time_interval = 0.04)
v1_4 = physical_pendulum_v1(FD = 0.99, total_time = 60, time_interval = 0.04)
v1_5 = physical_pendulum_v1(FD = 1.2, total_time = 60, time_interval = 0.04)

v1_1.calculate()
v1_2.calculate()
v1_3.calculate()
v1_4.calculate()
v1_5.calculate()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#Code for the using Latex in the tittle

plt.subplot(5,1,1)
plt.title((r'$\theta$ versus time'))
plt.plot(v1_1.t, v1_1.theta)
plt.ylabel(r'$F_D =0$')


plt.subplot(5,1,2)
plt.plot(v1_2.t, v1_2.theta)
plt.ylabel(r'$F_D =0.1$')

plt.subplot(5,1,3)
plt.plot(v1_3.t, v1_3.theta)
plt.ylabel(r'$F_D =0.5$,$\theta$ (radians)')

plt.subplot(5,1,4)
plt.plot(v1_4.t, v1_4.theta)
plt.ylabel(r'$F_D =0.99$')

plt.subplot(5,1,5)
plt.plot(v1_5.t, v1_5.theta)
plt.ylabel(r'$F_D =1.2$')
plt.xlabel("time (s)")

plt.xlim(0, 60)

plt.show()

v1_6 = physical_pendulum_v1_point_5(FD = 0, total_time = 60, time_interval = 0.04)
v1_7 = physical_pendulum_v1_point_5(FD = 0.1, total_time = 60, time_interval = 0.04)
v1_8 = physical_pendulum_v1_point_5(FD = 0.5, total_time = 60, time_interval = 0.04)
v1_9 = physical_pendulum_v1_point_5(FD = 0.99, total_time = 60, time_interval = 0.04)
v1_10 = physical_pendulum_v1_point_5(FD = 1.2, total_time = 60, time_interval = 0.04)

v1_6.calculate()
v1_7.calculate()
v1_8.calculate()
v1_9.calculate()
v1_10.calculate()

plt.subplot(5,1,1)
plt.plot(v1_6.t, v1_6.theta)

plt.subplot(5,1,2)
plt.plot(v1_7.t, v1_7.theta)

plt.subplot(5,1,3)
plt.plot(v1_8.t, v1_8.theta)

plt.subplot(5,1,4)
plt.plot(v1_9.t, v1_9.theta)

plt.subplot(5,1,5)
plt.plot(v1_10.t, v1_10.theta)

plt.xlim(0, 60)
plt.show()

v2_1 = physical_pendulum_v2(FD = 0, total_time = 60, time_interval = 0.04)
v2_2 = physical_pendulum_v2(FD = 0.1, total_time = 60, time_interval = 0.04)
v2_3 = physical_pendulum_v2(FD = 0.5, total_time = 60, time_interval = 0.04)
v2_4 = physical_pendulum_v2(FD = 0.99, total_time = 60, time_interval = 0.04)
v2_5 = physical_pendulum_v2(FD = 1.2, total_time = 60, time_interval = 0.04)

v2_1.calculate()
v2_2.calculate()
v2_3.calculate()
v2_4.calculate()
v2_5.calculate()

plt.subplot(5,1,1)
plt.plot(v2_1.t, v2_1.theta)

plt.subplot(5,1,2)
plt.plot(v2_2.t, v2_2.theta)

plt.subplot(5,1,3)
plt.plot(v2_3.t, v2_3.theta)

plt.subplot(5,1,4)
plt.plot(v2_4.t, v2_4.theta)

plt.subplot(5,1,5)
plt.plot(v2_5.t, v2_5.theta)

plt.xlim(0, 60)
plt.show()

v3_1 = physical_pendulum_v3(FD = 0, total_time = 60, time_interval = 0.04)
v3_2 = physical_pendulum_v3(FD = 0.1, total_time = 60, time_interval = 0.04)
v3_3 = physical_pendulum_v3(FD = 0.5, total_time = 60, time_interval = 0.04)
v3_4 = physical_pendulum_v3(FD = 0.99, total_time = 60, time_interval = 0.04)
v3_5 = physical_pendulum_v3(FD = 1.2, total_time = 60, time_interval = 0.04)

v3_1.calculate()
v3_2.calculate()
v3_3.calculate()
v3_4.calculate()
v3_5.calculate()

plt.subplot(5,1,1)
plt.plot(v3_1.t, v3_1.theta)
plt.xlim((0, 60))

plt.subplot(5,1,2)
plt.plot(v3_2.t, v3_2.theta)
plt.xlim((0, 60))

plt.subplot(5,1,3)
plt.plot(v3_3.t, v3_3.theta)
plt.xlim((0, 60))

plt.subplot(5,1,4)
plt.plot(v3_4.t, v3_4.theta)
plt.xlim((0, 60))

plt.subplot(5,1,5)
plt.plot(v3_5.t, v3_5.theta)
plt.xlim((0, 60))

plt.show()

#After I ploted this figure I found that there were some distinct differences between the calculation results of the two numerical methods, so I decides to put the curves of the two sets of results together to make further comparison.
#The differences are some obvious that I begin to doubt my program.:)

comparison_Euler_Cromer_1 = physical_pendulum_v1_point_5(FD = 0, total_time = 60, time_interval = 0.04)
comparison_Euler_Cromer_2 = physical_pendulum_v1_point_5(FD = 0.1, total_time = 60, time_interval = 0.04)
comparison_Euler_Cromer_3 = physical_pendulum_v1_point_5(FD = 0.5, total_time = 60, time_interval = 0.04)
comparison_Euler_Cromer_4 = physical_pendulum_v1_point_5(FD = 0.99, total_time = 60, time_interval = 0.04)
comparison_Euler_Cromer_5 = physical_pendulum_v1_point_5(FD = 1.2, total_time = 60, time_interval = 0.04)

comparison_Runga_Kutta_1 = physical_pendulum_v2_point_5(FD = 0, total_time = 60, time_interval = 0.04)
comparison_Runga_Kutta_2 = physical_pendulum_v2_point_5(FD = 0.1, total_time = 60, time_interval = 0.04)
comparison_Runga_Kutta_3 = physical_pendulum_v2_point_5(FD = 0.5, total_time = 60, time_interval = 0.04)
comparison_Runga_Kutta_4 = physical_pendulum_v2_point_5(FD = 0.99, total_time = 60, time_interval = 0.04)
comparison_Runga_Kutta_5 = physical_pendulum_v2_point_5(FD = 1.2, total_time = 60, time_interval = 0.04)

comparison_Verlet_1 = physical_pendulum_v3_point_5(FD = 0, total_time = 60, time_interval = 0.04)
comparison_Verlet_2 = physical_pendulum_v3_point_5(FD = 0.1, total_time = 60, time_interval = 0.04)
comparison_Verlet_3 = physical_pendulum_v3_point_5(FD = 0.5, total_time = 60, time_interval = 0.04)
comparison_Verlet_4 = physical_pendulum_v3_point_5(0.99, total_time = 60, time_interval = 0.04)
comparison_Verlet_5 = physical_pendulum_v3_point_5(FD = 1.2, total_time = 60, time_interval = 0.04)

comparison_Runga_Kutta_1.calculate()
comparison_Runga_Kutta_2.calculate()
comparison_Runga_Kutta_3.calculate()
comparison_Runga_Kutta_4.calculate()
comparison_Runga_Kutta_5.calculate()

comparison_Euler_Cromer_1.calculate()
comparison_Euler_Cromer_2.calculate()
comparison_Euler_Cromer_3.calculate()
comparison_Euler_Cromer_4.calculate()
comparison_Euler_Cromer_5.calculate()

comparison_Verlet_1.calculate()
comparison_Verlet_2.calculate()
comparison_Verlet_3.calculate()
comparison_Verlet_4.calculate()
comparison_Verlet_5.calculate()

plt.plot(comparison_Euler_Cromer_1.t, comparison_Euler_Cromer_1.theta, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_1.t, comparison_Runga_Kutta_1.theta, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_1.t, comparison_Verlet_1.theta, '-.', label = 'Verlet')
plt.title((r'$\theta$ versus time'))
plt.ylabel(r'$F_D =0$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()

plt.plot(comparison_Euler_Cromer_2.t, comparison_Euler_Cromer_2.theta, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_2.t, comparison_Runga_Kutta_2.theta, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_2.t, comparison_Verlet_2.theta, '-.', label = 'Verlet')
plt.title((r'$\theta$ versus time'))
plt.ylabel(r'$F_D =0.1$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()


plt.plot(comparison_Euler_Cromer_3.t, comparison_Euler_Cromer_3.theta, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_3.t, comparison_Runga_Kutta_3.theta, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_3.t, comparison_Verlet_3.theta, '-.', label = 'Verlet')
plt.title((r'$\theta$ versus time'))
plt.ylabel(r'$F_D =0.5$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()


plt.plot(comparison_Euler_Cromer_4.t, comparison_Euler_Cromer_4.theta, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_4.t, comparison_Runga_Kutta_4.theta, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_4.t, comparison_Verlet_4.theta, '-.', label = 'Verlet')
plt.title((r'$\theta$ versus time'))
plt.ylabel(r'$F_D =0.99$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()

plt.plot(comparison_Euler_Cromer_5.t, comparison_Euler_Cromer_5.theta, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_5.t, comparison_Runga_Kutta_5.theta, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_5.t, comparison_Verlet_5.theta, '-.', label = 'Verlet')
plt.title((r'$\theta$ versus time'))
plt.ylabel(r'$F_D =1.2$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()

#When the coeefficient of the drive force is 1.2, I find that the curves ploting through different methods differs from others greatly and exhit a susceptibility to different numerical methods.
#So I decide to change the time interval to see if this will reduce the differences.
comparison_Euler_Cromer_5_2 = physical_pendulum_v1_point_5(FD = 1.2, total_time = 60, time_interval = 0.02)
comparison_Runga_Kutta_5_2 = physical_pendulum_v2_point_5(FD = 1.2, total_time = 60, time_interval = 0.02)
comparison_Verlet_5_2 = physical_pendulum_v3_point_5(FD = 1.2, total_time = 60, time_interval = 0.02)

comparison_Euler_Cromer_5_2.calculate()
comparison_Runga_Kutta_5_2.calculate()
comparison_Verlet_5_2.calculate()

plt.plot(comparison_Euler_Cromer_5_2.t, comparison_Euler_Cromer_5_2.theta, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_5_2.t, comparison_Runga_Kutta_5_2.theta, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_5_2.t, comparison_Verlet_5_2.theta, '-.', label = 'Verlet')
plt.title((r'$\theta$ versus time, $\Delta t=0.02$(s)'))
plt.ylabel(r'$F_D =1.2$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()

comparison_Euler_Cromer_5_3 = physical_pendulum_v1_point_5(FD = 1.2, total_time = 60, time_interval = 0.01)
comparison_Runga_Kutta_5_3 = physical_pendulum_v2_point_5(FD = 1.2, total_time = 60, time_interval = 0.01)
comparison_Verlet_5_3 = physical_pendulum_v3_point_5(FD = 1.2, total_time = 60, time_interval = 0.01)

comparison_Euler_Cromer_5_3.calculate()
comparison_Runga_Kutta_5_3.calculate()
comparison_Verlet_5_3.calculate()

plt.plot(comparison_Euler_Cromer_5_3.t, comparison_Euler_Cromer_5_3.theta, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_5_3.t, comparison_Runga_Kutta_5_3.theta, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_5_3.t, comparison_Verlet_5_3.theta, '-.', label = 'Verlet')
plt.title((r'$\theta$ versus time, $\Delta t=0.01$(s)'))
plt.ylabel(r'$F_D =1.2$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()

#After I compare these three plot, I find that the high drive situation is not only sensitive to the numerical method, it is also highly sensitive to the time interval.
#The shape of curves in the three plots are different. First after I changed the time interval to a smaller one the three curves come closer to each others in the region close to the origin, but they still differs greatly when the time is large.
#As I continue to make the time interval smaller, the relative position continues to change in the third plots, this is the sensitivity to the time interval.

plt.plot(comparison_Euler_Cromer_1.t, comparison_Euler_Cromer_1.energy, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_1.t, comparison_Runga_Kutta_1.energy, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_1.t, comparison_Verlet_1.energy, '-.', label = 'Verlet')
plt.title((r'energy versus time'))
plt.ylabel(r'$F_D =0$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()

plt.plot(comparison_Euler_Cromer_2.t, comparison_Euler_Cromer_2.energy, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_2.t, comparison_Runga_Kutta_2.energy, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_2.t, comparison_Verlet_2.energy, '-.', label = 'Verlet')
plt.title((r'energy versus time'))
plt.ylabel(r'$F_D =0.1$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()


plt.plot(comparison_Euler_Cromer_3.t, comparison_Euler_Cromer_3.energy, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_3.t, comparison_Runga_Kutta_3.energy, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_3.t, comparison_Verlet_3.energy, '-.', label = 'Verlet')
plt.title((r'energy versus time'))
plt.ylabel(r'$F_D =0.5$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()


plt.plot(comparison_Euler_Cromer_4.t, comparison_Euler_Cromer_4.energy, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_4.t, comparison_Runga_Kutta_4.energy, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_4.t, comparison_Verlet_4.energy, '-.', label = 'Verlet')
plt.title((r'energy versus time'))
plt.ylabel(r'$F_D =0.99$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()

plt.plot(comparison_Euler_Cromer_5.t, comparison_Euler_Cromer_5.energy, '-', label = 'Euler-Cromer')
plt.plot(comparison_Runga_Kutta_5.t, comparison_Runga_Kutta_5.energy, '--', label = 'Runga-Kutta')
plt.plot(comparison_Verlet_5.t, comparison_Verlet_5.energy, '-.', label = 'Verlet')
plt.title((r'energy versus time'))
plt.ylabel(r'$F_D =1.2$')
plt.xlabel("time (s)")
plt.xlim(0, 60)
plt.legend(loc ='best')
plt.show()

#First step:plot the phase diagram, use the results of Runga-Kutta method

phase_diagram_1 = physical_pendulum_v2(FD = 0, total_time = 500, time_interval = 0.01)
phase_diagram_2 = physical_pendulum_v2(FD = 0.1, total_time = 500, time_interval = 0.01)
phase_diagram_3 = physical_pendulum_v2(FD = 0.5, total_time = 500, time_interval = 0.01)
phase_diagram_4 = physical_pendulum_v2(FD = 0.99, total_time = 500, time_interval = 0.01)
phase_diagram_5 = physical_pendulum_v2(FD = 1.2, total_time = 500, time_interval = 0.01)

phase_diagram_1.calculate()
phase_diagram_2.calculate()
phase_diagram_3.calculate()
phase_diagram_4.calculate()
phase_diagram_5.calculate()

plt.plot(phase_diagram_1.theta, phase_diagram_1.omega, ':', label = 'Runga-Kutta')
plt.title((r'$\omega$ versus $\theta$ $F_D=0$'))
plt.ylabel(r'$\omega$ (radians/s)')
plt.xlabel(r"$\theta$ (radian)")
plt.show()

plt.plot(phase_diagram_2.theta, phase_diagram_2.omega, ':', label = 'Runga-Kutta')
plt.title((r'$\omega$ versus $\theta$ $F_D=0.1$'))
plt.ylabel(r'$\omega$ (radians/s)')
plt.xlabel(r"$\theta$ (radian)")
plt.show()

plt.plot(phase_diagram_3.theta, phase_diagram_3.omega, ':', label = 'Runga-Kutta')
plt.title((r'$\omega$ versus $\theta$ $F_D=0.5$'))
plt.ylabel(r'$\omega$ (radians/s)')
plt.xlabel(r"$\theta$ (radian)")
plt.show()

plt.plot(phase_diagram_4.theta, phase_diagram_4.omega, ':', label = 'Runga-Kutta')
plt.title((r'$\omega$ versus $\theta$ $F_D=0.99$'))
plt.ylabel(r'$\omega$ (radians/s)')
plt.xlabel(r"$\theta$ (radian)")
plt.show()

plt.scatter(phase_diagram_5.theta, phase_diagram_5.omega,alpha = 0.03, linewidth = 0)
plt.title((r'$\omega$ versus $\theta$ $F_D=1.2$'))
plt.ylabel(r'$\omega$ (radians/s)')
plt.xlabel(r"$\theta$ (radian)")
plt.show()

#Then plot then Poicare section
Poincare_section = physical_pendulum_v2(FD = 1.2, total_time = 2000, time_interval = 0.01)
Poincare_section.calculate()

omega_in_phase = []
theta_in_phase = []

for i in range(len(Poincare_section.t)):
    if ((2 / 3 * Poincare_section.t[i]) % (2 * math.pi)) <= (2 / 3 * Poincare_section.dt * 1) or (2 * math.pi - ((2 / 3 * Poincare_section.t[i]) % (2 * math.pi))) <= (2 / 3 * Poincare_section.dt * 1):
        omega_in_phase.append(Poincare_section.omega[i])
        theta_in_phase.append(Poincare_section.theta[i])

plt.plot(theta_in_phase, omega_in_phase, ':')
plt.title((r'Poincar\'{e} section $\omega$ versus $\theta$ $F_D=1.2$'))
plt.ylabel(r'$\omega$ (radians/s)')
plt.xlabel(r"$\theta$ (radian)")
