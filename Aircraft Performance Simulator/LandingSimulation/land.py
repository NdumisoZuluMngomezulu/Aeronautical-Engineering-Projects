import math
import matplotlib.pyplot as plt

weight = 60000
mass = weight / 9.81

wing_area = 16.2
cd = 0.3

landing_speed = 65

brake_force = 10000
reverse_thrust = 8000

rho = 1.225

dt = 0.1

velocity = landing_speed
distance = 0

distances = []
velocities = []

while velocity > 0:

    drag = 0.5 * rho * velocity**2 * wing_area * cd

    stopping_force = (
        brake_force
        + reverse_thrust
        + drag
    )

    acceleration = stopping_force / mass

    velocity -= acceleration * dt

    if velocity < 0:
        velocity = 0

    distance += velocity * dt

    distances.append(distance)
    velocities.append(velocity)

print(f"Landing distance: {distance:.1f} m")

plt.plot(distances, velocities)
plt.xlabel("Distance (m)")
plt.ylabel("Speed (m/s)")
plt.title("Landing Roll")
plt.grid()
plt.show()