import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05


plt.figure(figsize=(6, 4), dpi=150)

for v in range(0, 101, 10):   # 0,10,20,...100
    recovered=0
    vaccinated = int(N * v / 100)
    if vaccinated == N:
        infected = 0
        susceptible = 0
    else:
        infected = 1
        susceptible = N - vaccinated - infected

    i_history = [infected]

    for days in range(1000):
        
        IP = min(beta * infected / N, 1)

        new_infections = np.random.choice(
            [0, 1],
            size=susceptible,
            p=[1 - IP, IP]
        ).sum()

        new_recoveries = np.random.choice(
            [0, 1],
            size=infected,
            p=[1 - gamma, gamma]
        ).sum()

        susceptible -= new_infections
        infected += new_infections - new_recoveries
        recovered += new_recoveries

        i_history.append(infected)

    time = np.arange(len(i_history))
    plt.plot(time, i_history, label=f"{v}%")

plt.xlabel("time")
plt.ylabel("number of infected people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.show()
