
import numpy as np
import matplotlib.pyplot as plt


D = 100 # diffusivity 
Lx = 300 # model domain 


dx = 0.5 # grid spacing 
x = np.arange(start=0, stop=Lx, step=dx)
nx = len(x)  # number of grid nodes


z = np.zeros_like(x) # create an array LIKE x -- 600 variables
z_left = 500  # left side of domain
z_right = 0   # right side of domain
z[x<= Lx/2] = z_left # z for values of x less than or equal do half the domain = 500
z[x> Lx/2] = z_right  # z for values of x greater than half the domain = 0


plt.figure()  # figure window set up
plt.plot(x,z, "r")
plt.xlabel("x")
plt.ylabel("z")
plt.title("Initial hillslope profile")


nt = 5000 # number of time steps 
dt = 0.5 * dx**2/D  # time step (seconds)


for t in range(0, nt):
	z[1:-1] += D * dt / dx ** 2 * (z[:-2] - 2*z[1:-1] + z[2:])


plt.figure()  # figure window set up
plt.plot(x,z, "b")
plt.xlabel("x")
plt.ylabel("z")
plt.title("Final hillslope profile")

