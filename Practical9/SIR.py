import numpy as np
import matplotlib.pyplot as plt

N=10000
infected=1
beta=0.3
gamma=0.05
days=0
susceptible = N-infected
recovered=0

s_history = [susceptible]
i_history = [infected]
r_history = [recovered]


for days in range(0,1000):
    IP= min(beta * infected/N,1)
    new_infections=np.random.choice(
            [0, 1],
            size=susceptible,
            p=[1 - IP, IP],
    ).sum()       
    new_recoveries = np.random.choice(
            [0, 1],
            size=infected,
            p=[1 - gamma, gamma],
     ).sum()
    
    susceptible -= new_infections
    infected += new_infections - new_recoveries
    recovered += new_recoveries

    s_history.append(susceptible)
    i_history.append(infected)
    r_history.append(recovered)

time = np.arange(len(s_history))
s = s_history
i = i_history
r = r_history

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(time, s, label="susceptible")
plt.plot(time, i, label="infected")
plt.plot(time, r, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.show()







