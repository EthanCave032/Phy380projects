import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("fismflux20020824.dat", skiprows=1)

# times


hours = data[:,3]

minutes = data[:,4]

time = 60 * hours + minutes

# irradiance

irrandiance = data[:,61]

plt.plot(time,irrandiance)
plt.xlabel("Time since midnight (minutes)")
plt.ylabel("Spectral irradiance (W/m²/nm)")
plt.title("Solar EUV irradiance in bin 56, August 24, 2002")
plt.show()