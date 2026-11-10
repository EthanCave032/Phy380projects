import numpy as np
import matplotlib.pyplot as plt

h = 1e-2
A = 10
a = 2
k = 0.4

x = np.arange(0,20,0.1)

def function(x):
    return A * np.cos((np.pi * x)/a) * np.e ** (-k*x)
    
def derivative(x):
    derivative = ((function(x + h) - function(x))) / h
    return derivative

def derivativebutbetternow(x):
    derivativebutbetternow = ((function(x + h) - function(x -h)) / (2 * h))
    return derivativebutbetternow
def check(x):
    angle = np.pi * x / a
    return A * np.exp(-k * x) * (
        -k * np.cos(angle) - (np.pi / a) * np.sin(angle)
    )
x_test = np.pi / 4
print(function(x_test))
print(derivative(x_test),"error first order:",check(x_test) - derivative(x_test))
print(derivativebutbetternow(x_test),"error second order:",check(x_test)-derivativebutbetternow(x_test))
print(check(x_test))

# figure for 1

plt.figure()
plt.plot(x, function(x), color="blue")
plt.xlabel("Position x (m)")
plt.ylabel("Electric field E (V/m)")
plt.title("Electric field along the waveguide")
plt.show()

# figure for 2a, 2b, 2c

plt.figure()
plt.plot(x, check(x), color="black", label="Analytic")
plt.plot(x, derivative(x), "--", label="Forward difference")
plt.plot(x, derivativebutbetternow(x), ":", label="Central difference")
plt.xlabel("Position x (m)")
plt.ylabel("dE/dx (V/m²)")
plt.legend()
plt.show()

# figure for 2d, central differencing has less error by about 2 orders of magnetude

plt.figure()
plt.semilogy(x, abs(check(x) - derivative(x)), label="Forward difference")
plt.semilogy(x, abs(check(x) - derivativebutbetternow(x)), label="Central difference")
plt.xlabel("Position x (m)")
plt.ylabel("Absolute error (V/m²)")
plt.legend()
plt.show()

# figure for 2e, differencing with h/Δx = 0.05 m

h = 0.05
x = np.arange(0, 20, 0.1)

plt.figure()
plt.semilogy(x, abs(derivative(x) - check(x)), label="Forward difference")
plt.semilogy(x, abs(derivativebutbetternow(x) - check(x)), label="Central difference")
plt.xlabel("Position x (m)")
plt.ylabel("Absolute error (V/m²)")
plt.title("Derivative errors for Δx = 0.05 m")
plt.legend()
plt.show()

#figure for part f, loglog plot of Δx vs. error values
# the reason that the error starts to grow at smaller h values is because of pythons floating point errors, when you add the value in (x+h)
# or (x-h) python will approximate it and cause a floating point error, these errors get worse as you get smaller.

x_test = 1.0
step_sizes = []
errors = []

for power in range(1, 16):
    h = 10.0 ** (-power)
    error = abs(derivative(x_test) - check(x_test))

    step_sizes.append(h)
    errors.append(error)

plt.figure()
plt.loglog(step_sizes, errors, "o-")
plt.xlabel("Step size h (m)")
plt.ylabel("Absolute error (V/m²)")
plt.title("Forward-difference error at x = 1 m")
plt.grid(True, which="both", alpha=0.3)
plt.show()
