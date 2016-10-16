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
