import random

results = []

for i in range(10000):

    weight = random.uniform(
        50000,
        70000
    )

    temperature = random.uniform(
        0,
        40
    )

    wind = random.uniform(
        -10,
        15
    )

    runway_distance = simulate_takeoff(
        weight,
        temperature,
        wind
    )

    results.append(runway_distance)

overruns = 0

runway_length = 1800

for distance in results:

    if distance > runway_length:
        overruns += 1

risk = overruns / len(results)

print(
    f"Runway Overrun Risk: "
    f"{risk*100:.2f}%"
)