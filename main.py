from Pendulum import Pendulum
dt = 0.01
time = 10
pendulum_length = 10
p1 = Pendulum(pendulum_length)
p1.euler_formula(dt, time)
