import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

df = pd.read_csv("takeoff_data.csv")

X = df[
    [
        "weight",
        "wind",
        "temperature",
        "slope"
    ]
]

y = df["distance"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2
)

model = RandomForestRegressor(
    n_estimators=200
)

model.fit(X_train, y_train)

score = model.score(X_test, y_test)

print("R² Score:", score)

prediction = model.predict([
    [
        85000,  # weight
        5,      # headwind
        25,     # temperature
        0.5     # slope
    ]
])

print(
    f"Predicted Takeoff Distance: "
    f"{prediction[0]:.1f} m"
)