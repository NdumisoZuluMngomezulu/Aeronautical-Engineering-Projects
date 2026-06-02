import math
import matplotlib.pyplot as plt

# Aircraft
weight = 60000          # N
wing_area = 16.2        # m²
cl = 1.2
cd = 0.04
thrust = 18000          # N

rho = 1.225
g = 9.81

mass = weight / g

velocity = 80           # m/s after takeoff
altitude = 0

dt = 0.5

times = []
altitudes = []

time = 0

while altitude < 3000:

    drag = 0.5 * rho * velocity**2 * wing_area * cd

    excess_power = (thrust - drag) * velocity

    roc = excess_power / weight

    altitude += roc * dt

    time += dt

    times.append(time)
    altitudes.append(altitude)

print(f"Reached 3000 m in {time:.1f} seconds")

plt.plot(times, altitudes)
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Aircraft Climb Profile")
plt.grid()
plt.show()