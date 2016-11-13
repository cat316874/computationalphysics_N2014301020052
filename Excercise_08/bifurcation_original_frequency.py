import math
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#Code for the using Latex in the tittle

class bifurcation_diagram:
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
            plt.xlim(1.35,1.5)
            plt.ylim(1,3)
            plt.xlabel("$F_D$")
            plt.ylabel(r'$\theta$(radians)')
            plt.title(r'Bifurcation diagram $\theta$ versus $F_D$')
        plt.show()

a1 = bifurcation_diagram(total_time = 4000, time_interval = 0.01, driving_force_interval = 0.001)
a1.calculate()
