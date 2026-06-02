import matplotlib.pyplot as plt

plt.hist(
    results,
    bins=50
)

plt.xlabel(
    "Takeoff Distance"
)

plt.ylabel(
    "Occurrences"
)

plt.title(
    "Monte Carlo Takeoff Analysis"
)

plt.show()