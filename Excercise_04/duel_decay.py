import pylab as pl
import math

class duel_decay:
    """docstring for "duel decay". Programmed by Yuan Tian."""
    def __init__(self, number_of_nuclei_nA = 100, number_of_nuclei_nB = 0, time_costant = 1, time_of_duration = 5, time_interval = 0.05):
        self.nA = [number_of_nuclei_nA]
        self.nB = [number_of_nuclei_nB]
        self.t = [0]
        self.tau = time_costant
        self.dt = time_interval
        self.time = time_of_duration
        self.steps = int(time_of_duration // time_interval + 1)
        print('Initial number of type A nuclei ->', number_of_nuclei_nA)
        print('Initial number of type B nuclei ->', number_of_nuclei_nB)
        print('Time interval ->', time_interval)
        print('Total time ->', time_of_duration)
    def calculate(self):
        for i in range(self.steps):
            tmp_A = self.nA[i] + (self.nB[i] - self.nA[i]) / self.tau * self.dt
            tmp_B = self.nB[i] + (self.nA[i] - self.nB[i]) / self.tau * self.dt
            self.nA.append(tmp_A)
            self.nB.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.nA, 'b', label = 'Number of Nuclei A')
        pl.plot(self.t, self.nB, 'r', label = 'Number of Nuclei B')
        pl.title('Change of Nuclei Relative to the Time')
        pl.xlabel('time $s$')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc = 'best')
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.nA[i], self.nB[i], file = myfile)
        myfile.close()


a = duel_decay()
a.calculate()
a.show_results()
a.store_results()

class exact_result_check(duel_decay):
    def show_results(self):
        self.etA = []
        self.etB = []
        for i in range(len(self.t)):
            temp_A = 50 * math.exp(-2 * self.t[i] / self.tau) + 50
            temp_B = -50 * math.exp(-2 * self.t[i] / self.tau) + 50
            self.etA.append(temp_A)
            self.etB.append(temp_B)
        pl.plot(self.t, self.etA, 'b', label = 'A-analytical')
        pl.plot(self.t, self.nA, '*', label = 'A-numerical')
        pl.plot(self.t, self.etB, 'r', label = 'B-analytical')
        pl.plot(self.t, self.nB, 'x', label = 'B-numerical')
        pl.xlabel('time $s$')
        pl.ylabel('Number of Nuclei')
        pl.xlim(0, self.time)
        pl.legend(loc = 'best')
        pl.show()

b = exact_result_check(time_interval = 0.2)
b.calculate()
b.show_results()

class diff_step_check(duel_decay):
    def show_results(self, style):
        pl.plot(self.t, self.nA, style)
        pl.plot(self.t, self.nB, style)
        pl.xlabel('time $s$')
        pl.ylabel('Number of Nuclei')
        pl.xlim(0, self.time)

c = diff_step_check(time_interval = 0.05)
c.calculate()
c.show_results('b')

d = diff_step_check(time_interval = 0.1)
d.calculate()
d.show_results('g')

e = diff_step_check(time_interval = 0.2)
e.calculate()
e.show_results('y')

f = diff_step_check(time_interval = 0.25)
f.calculate()
f.show_results('m')
