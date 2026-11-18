import numpy as np
import matplotlib.pyplot as plt
# varibles

T0 = 100
sigma = 1
dx = 0.1
dy = 0.1

# part A

x=np.arange(-3,3+dx,dx)
y=np.arange(-3,3+dy,dy)
X,Y = np.meshgrid(x,y)

Temp = T0 * np.exp(-(X**2 + Y**2) / sigma**2)

plt.figure()
plate = plt.contourf(x, y, Temp, levels=40)
plt.colorbar(plate, label="Temperature (K)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Temperature on the heated plate")
plt.savefig("t_plate.png")

# part B

dTx = (Temp[1:-1, 2:] - Temp[1:-1, :-2]) / (2 * dx)
dTy = (Temp[2:, 1:-1] - Temp[:-2, 1:-1]) / (2 * dy)


#Part C

dTy_numpy, dTx_numpy = np.gradient(Temp, dy, dx)

#Part D

numpy_slope = dTx_numpy[30, :]  # y = 0 in the full grid
central_slope = dTx[29, :]      # y = 0 in the trimmed grid

exact = (-2 * x / sigma**2) * T0 * np.exp(-x**2 / sigma**2)

plt.figure()
plt.plot(x, exact, label="Analytic")
plt.plot(x[1:-1], dTx[29, :], "--", label="Central difference")
plt.plot(x, dTx_numpy[30, :], ".", label="Numpy gradient")

plt.xlabel("x (m)")
plt.ylabel("∂T/∂x (K/m)")
plt.title("Temperature slope along y = 0")
plt.legend()
plt.savefig("dtdx.png")
plt.show()

#max difference (i)

diff_x = np.abs(dTx - dTx_numpy[1:-1, 1:-1])
diff_y = np.abs(dTy - dTy_numpy[1:-1, 1:-1])

print("Largest x difference:", np.max(diff_x), "K/m")
print("Largest y difference:", np.max(diff_y), "K/m")

#since the error is the same we know that np.gradient uses the same central differencing method that we used.

#(ii)

exact_x = (-2 * X / sigma**2) * Temp
error_x = np.abs(dTx_numpy - exact_x)

print("Max error on left/right edges:", np.max(error_x[:, [0, -1]]))
print("Max error in the interior:", np.max(error_x[1:-1, 1:-1]))

#using this method we find 
# Max error on left/right edges: 0.025174170380201644
# Max error in the interior: 0.6463468595502917
# at the edges numpy uses forward and backward differencing so it can estimate the edges better then we can.
# we get a truckcation error because our method cuts off these data points when trying to use central differencing

# part E
plt.figure()

plate = plt.contourf(X, Y, Temp, levels=25)
plt.colorbar(plate, label="Temperature (K)")

plt.quiver(
    X[::5, ::5], Y[::5, ::5],
    -dTx_numpy[::5, ::5], -dTy_numpy[::5, ::5],
    color="cyan", angles="xy"
)

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Heat flow on the plate")
plt.show()



