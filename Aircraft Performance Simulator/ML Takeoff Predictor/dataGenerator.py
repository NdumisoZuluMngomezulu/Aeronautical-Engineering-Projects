import pandas as pd
import random

data = []

for i in range(5000):

    weight = random.uniform(50000, 120000)

    wind = random.uniform(-15, 15)

    temperature = random.uniform(-10, 40)

    slope = random.uniform(-2, 2)

    takeoff_distance = (
        0.025 * weight
        - 15 * wind
        + 8 * temperature
        + 200 * slope
    )

    data.append([
        weight,
        wind,
        temperature,
        slope,
        takeoff_distance
    ])

df = pd.DataFrame(
    data,
    columns=[
        "weight",
        "wind",
        "temperature",
        "slope",
        "distance"
    ]
)

df.to_csv("takeoff_data.csv", index=False)