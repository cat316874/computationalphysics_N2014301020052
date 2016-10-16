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
