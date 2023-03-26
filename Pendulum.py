import math

import numpy as np
import matplotlib.pyplot as plt


class Pendulum:
    def __init__(self, l, alpha=130, g=9.81):
        self.alpha = math.radians(alpha)
        # self.v = v
        # self.a = 0
        # self.q = q
        self.l = l
        self.g = g
        self.omega = 0
        self.epsilon = (-math.sin(self.alpha)*self.g)/self.l

    def calc_alpha(self, dt):
        return self.alpha + self.omega * dt

    def calc_omega(self, dt):
        return self.omega + self.epsilon * dt

    def calc_epsilon(self):
        print(f'calc_e {math.sin(self.alpha)}')
        return (-math.sin(self.alpha) * self.g) / self.l

    def coordinates(self):
        x = self.l * math.cos(self.alpha-(math.pi/2))
        y = self.l * math.sin(self.alpha-(math.pi/2))

        return x, y

    def euler_formula(self, dt, time):
        steps = time / dt
        times = [0]
        x_positions = [self.coordinates()[0]]
        y_positions = [self.coordinates()[1]]

        for moment in range(int(steps)):
            times.append((times[-1] + dt))
            self.epsilon = self.calc_epsilon()
            self.omega = self.calc_omega(dt)
            self.alpha = self.calc_alpha(dt)
            print(self.coordinates())
            print(f'E: {self.epsilon}\t w: {self.omega}\t a:{math.degrees(self.alpha)}')

            x_positions.append(self.coordinates()[0])
            y_positions.append(self.coordinates()[1])

        interp_t = np.linspace(0, times[-1], len(x_positions))
        interp_x_positions = np.interp(interp_t, times, x_positions)
        interp_y_positions = np.interp(interp_t, times, y_positions)
        plt.plot(interp_x_positions, interp_y_positions, color='#F5A9B8', alpha=0.8)

        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.axis('square')
        plt.title('Projectile Trajectory')
        plt.show()
