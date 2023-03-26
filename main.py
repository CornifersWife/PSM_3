# s24435 Maciej Łatosz
from Pendulum import Pendulum
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def show_movement(times, interp_t, x_positions, y_positions, color='#F5A9B8', ):
    fig, ax = plt.subplots()
    ax.set_xlim(min(x_positions) * 1.5, max(x_positions) * 1.5)
    ax.set_ylim(min(y_positions) * 1.5, max(y_positions) * 1.5)
    ax.set_aspect('equal')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_title('Projectile Trajectory')

    line, = ax.plot([], [], 'o', color=color, markersize=1)
    start, = ax.plot([], [], 'o', color='black', markersize=10)
    end, = ax.plot([], [], 'o', color=color, markersize=6)
    line_between_points, = ax.plot([], [], color=color, alpha=0.5)

    def animate(i):
        interp_x_positions = np.interp(interp_t[:i + 1], times, x_positions)
        interp_y_positions = np.interp(interp_t[:i + 1], times, y_positions)
        line.set_data(interp_x_positions, interp_y_positions)
        start.set_data([0], [0])
        end.set_data([interp_x_positions[-1]], [interp_y_positions[-1]])
        line_between_points.set_data([0, interp_x_positions[-1]], [0, interp_y_positions[-1]])

    ani = FuncAnimation(fig, animate, frames=len(interp_t), interval=33, repeat=False)
    plt.show()

##parameters
dt = 0.2
time = 100
pendulum_length = 1
angle = 170
##

p1 = Pendulum(pendulum_length, angle)
p2 = Pendulum(pendulum_length, angle)
p3 = Pendulum(pendulum_length, angle)
res_normal = p2.euler_formula(dt, time)
res_imp = p1.euler_formula(dt, time, True)
res_rk4 = p3.rk4_formula(dt, time)

show_movement(*res_normal, color="#303088")  # normal blue
show_movement(*res_imp, color='#F5A9B8')  # improved, pink
show_movement(*res_rk4, color="#308830")  # rk green
