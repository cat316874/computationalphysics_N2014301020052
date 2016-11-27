import math
import matplotlib.pyplot as plt

class central_force:
    def __init__(self, x0, y0, vx0, vy0, beta, time_interval, total_time):
        self.beta = beta
        self.steps = int(total_time // time_interval) + 1
        self.dt = time_interval
        self.t = [0]
        self.x = [x0]
        self.y = [y0]
        self.vx = [vx0]
        self.vy = [vy0]
    def calculate(self):
        for i in range(self.steps):
            r_temporary = math.sqrt(self.x[i] ** 2 + self.y[i] ** 2)
            vx_temporary = self.vx[i] - (4 * math.pi ** 2 * self.x[i]) / r_temporary ** (self.beta + 1) * self.dt
            vy_temporary = self.vy[i] - (4 * math.pi ** 2 * self.y[i]) / r_temporary ** (self.beta + 1) * self.dt
            x_temporary = self.x[i] + vx_temporary * self.dt
            y_temporary = self.y[i] + vy_temporary * self.dt
            self.t.append(self.t[i] + self.dt)
            self.vx.append(vx_temporary)
            self.vy.append(vy_temporary)
            self.x.append(x_temporary)
            self.y.append(y_temporary)

t1 = central_force(x0 = 1, y0 = 0, vx0 = 0, vy0 = 2 * math.pi - 0.5, time_interval = 0.01, total_time = 100, beta = 3)
t1.calculate()

plt.plot(t1.x, t1.y,'b.')
plt.axis('equal')
plt.title('beta = 3,v_{y0} = 2\pi')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
