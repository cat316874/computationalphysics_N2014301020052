import math
import matplotlib.pyplot as plt

class central_force:
    def __init__(self, eccentricity, theta0, time_interval, total_time):
        self.steps = int(total_time // time_interval) + 1
        self.dt = time_interval
        self.t = [0]
        self.x = [1]
        self.y = [0]
        self.vx = [0]
        vy0 = 2 * math.pi * math.sqrt(1 - eccentricity)
        self.vy = [vy0]
        self.omega = [0]
        self.theta = [theta0]
        self.duriation = 1 / math.sqrt((1 + eccentricity) ** 3)
        self.theta_in_phase = []
        self.omega_in_phase = []
    def calculate(self):
        for i in range(self.steps):
            r_temporary = math.sqrt(self.x[i] ** 2 + self.y[i] ** 2)
            vx_temporary = self.vx[i] - (4 * math.pi ** 2 * self.x[i]) / r_temporary ** 3 * self.dt
            vy_temporary = self.vy[i] - (4 * math.pi ** 2 * self.y[i]) / r_temporary ** 3 * self.dt
            x_temporary = self.x[i] + vx_temporary * self.dt
            y_temporary = self.y[i] + vy_temporary * self.dt
            self.t.append(self.t[i] + self.dt)
            self.vx.append(vx_temporary)
            self.vy.append(vy_temporary)
            self.x.append(x_temporary)
            self.y.append(y_temporary)
            omega_temporary =  self.omega[i] - 3 * 4 * math.pi ** 2 / r_temporary ** 5 * (x_temporary * math.sin(self.theta[i]) - y_temporary * math.cos(self.theta[i])) * (x_temporary * math.cos(self.theta[i]) + y_temporary * math.sin(self.theta[i])) * self.dt
            theta_temporary = self.theta[i] + omega_temporary * self.dt
            while theta_temporary > math.pi:
                theta_temporary = theta_temporary - 2 * math.pi
            while theta_temporary <= -math.pi:
                theta_temporary = theta_temporary + 2 * math.pi
            self.omega.append(omega_temporary)
            self.theta.append(theta_temporary)
    def calculate_in_phase(self):
        for i in range(self.steps):
            if self.t[i] % self.duriation < self.dt * 0.5 or (self.duriation - self.t[i] % self.duriation) < self.dt * 0.5:
                self.theta_in_phase.append(self.theta[i])
                self.omega_in_phase.append(self.omega[i])
