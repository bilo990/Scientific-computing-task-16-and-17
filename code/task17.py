import numpy as np
import matplotlib.pyplot as plt

# Pharmacokinetic Parameters
C_initial = 100.0  # mg/L
k_elimination = 0.15  # 1/hour
h = 0.5  # time step in hours
end_time = 24.0

def elimination_rate(C):
    return -k_elimination * C

time = np.arange(0, end_time + h, h)
concentration = np.zeros_like(time)
concentration[0] = C_initial

# Euler update loop
for i in range(len(time) - 1):
    concentration[i+1] = concentration[i] + h * elimination_rate(concentration[i])

# Exact analytical solution: C(t) = C0 * exp(-k_e * t)
exact_concentration = C_initial * np.exp(-k_elimination * time)

print(f"Euler estimated concentration after 24 hours: {concentration[-1]:.4f} mg/L")
print(f"Exact concentration after 24 hours: {exact_concentration[-1]:.4f} mg/L")
print(f"Absolute Error: {abs(concentration[-1] - exact_concentration[-1]):.4f} mg/L")

# Plot results
plt.plot(time, concentration, 'o--', label="Euler Method")
plt.plot(time, exact_concentration, label="Exact Elimination Curve")
plt.xlabel("Time (hours)")
plt.ylabel("Drug Concentration (mg/L)")
plt.title("Drug Elimination from Bloodstream (Euler Method)")
plt.legend()
plt.grid(True)
plt.show()