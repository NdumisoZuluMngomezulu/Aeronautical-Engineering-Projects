import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=distances,
        y=velocities,
        mode="lines",
        name="Velocity"
    )
)

fig.update_layout(
    title="Takeoff Roll",
    xaxis_title="Distance (m)",
    yaxis_title="Velocity (m/s)"
)

fig.show()