import numpy as np
import matplotlib.pyplot as plt

# =====================
# Pseudocode / plan
# =====================
# 1. Make a 100 x 100 population grid.
#    0 = susceptible, 1 = infected, 2 = recovered.
# 2. Randomly choose one person to be infected at the start.
# 3. For 100 time steps:
#    a. Find all currently infected cells.
#    b. For each infected cell, check its 8 neighbouring cells.
#    c. If a neighbour is susceptible, infect it with probability beta.
#    d. The infected cell recovers with probability gamma.
#    e. Store selected time points so we can plot the disease spread.
# 4. Plot snapshots of the population at times 0, 10, 50, and 100.

# Model parameters
beta = 0.3
gamma = 0.05
time_steps = 100

# Make array of all susceptible population
population = np.zeros((100, 100), dtype=int)

# Randomly choose one infected individual
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# Save snapshots for plotting later
snapshot_times = [0, 10, 50, 100]
snapshots = {0: population.copy()}

# These are the 8 possible neighbour directions around a cell
neighbour_directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

# Run the spatial SIR model
for t in range(1, time_steps + 1):
    new_population = population.copy()

    infected_points = np.where(population == 1)

    for x, y in zip(infected_points[0], infected_points[1]):

        # Try to infect each of the 8 neighbours
        for dx, dy in neighbour_directions:
            nx = x + dx
            ny = y + dy

            # Check that the neighbour is inside the grid
            if 0 <= nx < 100 and 0 <= ny < 100:
                # Only susceptible neighbours can be infected
                if population[nx, ny] == 0:
                    if np.random.random() < beta:
                        new_population[nx, ny] = 1

        # Infected individual can recover
        if np.random.random() < gamma:
            new_population[x, y] = 2

    population = new_population

    if t in snapshot_times:
        snapshots[t] = population.copy()

# Plot the selected snapshots
plt.figure(figsize=(8, 8), dpi=150)

for plot_number, t in enumerate(snapshot_times, start=1):
    plt.subplot(2, 2, plot_number)
    plt.imshow(
        snapshots[t],
        cmap="viridis",
        interpolation="nearest",
        vmin=0,
        vmax=2
    )
    plt.title(f"time = {t}")
    plt.xticks([])
    plt.yticks([])

plt.suptitle("Spatial SIR model")
plt.tight_layout()
plt.show()
