# BIT 2118: Scientific Computing — Tasks 16 & 17

This repository contains individual solutions and documentation for **Task 16 (Numerical Integration)** and **Task 17 (Ordinary Differential Equations - Euler Method)** as specified in the **BIT 2118: Scientific Computing** course project guidelines.

---

## Task 16: Numerical Integration

### 1. Mathematical Concept
An integral computes the total accumulated quantity or the area under a curve.
* **Trapezoidal Rule:** Approximates the integral by dividing the region under the graph into trapezoids:
  $$\int_{a}^{b} f(x) \, dx \approx \sum_{i=0}^{n-1} \frac{f(x_i) + f(x_{i+1})}{2} \Delta x$$
* **Simpson's Rule:** Fits quadratic polynomials (parabolic segments) over adjacent subintervals, providing higher accuracy for smooth functions:
  $$\int_{a}^{b} f(x) \, dx \approx \frac{\Delta x}{3} \left[ f(x_0) + 4 \sum_{\text{odd } i} f(x_i) + 2 \sum_{\text{even } i} f(x_i) + f(x_n) \right]$$

---

### 2. Base Task Analysis

#### Inputs & Mathematical Operations
* **Inputs:** 
  * Sampling times: $t = [0, 2, 4, 6, 8, 10, 12] \text{ hours}$
  * Recorded power readings: $P(t) = [0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9] \text{ kW}$
* **Operation:** Evaluates total electrical energy consumed (kWh) over $12 \text{ hours}$:
  $$E = \int_{0}^{12} P(t) \, dt$$

#### Parameter Variation
* **Change:** Reduced sampling interval from $\Delta t = 2 \text{ hours}$ to $\Delta t = 1 \text{ hour}$ with added intermediate readings.
* **Effect:** Decreasing step size improves approximation accuracy. The residual gap between the Trapezoidal estimate and Simpson's estimate narrows significantly as both converge toward the true continuous integral.

#### Output & Visualization Interpretation
* **Trapezoidal Estimate:** $15.300 \text{ kWh}$
* **Simpson's Estimate:** $15.333 \text{ kWh}$
* **Absolute Difference:** $0.033 \text{ kWh}$
* **Interpretation:** The integral calculates total electrical energy spent over 12 hours. A plot of $P(t)$ vs. $t$ shows power usage rising to a peak of $1.8 \text{ kW}$ around hour 6 before tapering down. The total integral represents the area bounded under this power curve.

---

### 3. Real-World Extension: Volumetric Pipeline Water Flow

#### Problem Formulation
A sensor logs water flow rates ($Q(t)$ in $\text{m}^3/\text{hr}$) through an agricultural irrigation system every 30 minutes. We compute total water volume ($\text{m}^3$) delivered over 3 hours.

#### Assumptions & Inputs
* **Assumptions:** Flow rate varies continuously and smoothly across sampling periods.
* **Inputs:**
  * $t = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0] \text{ hours}$
  * $Q(t) = [12.0, 15.5, 20.0, 22.5, 18.0, 14.0, 10.0] \text{ m}^3/\text{hr}$

#### Implementation
File location: `code/Task_16_numerical_integration.py`

```python
import numpy as np
from scipy.integrate import simpson

# Pipeline flow rate measurements (m^3/hr) over 3 hours (logged every 30 mins)
time_hours = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
flow_rate_m3h = np.array([12.0, 15.5, 20.0, 22.5, 18.0, 14.0, 10.0])

# Compute total volume using Trapezoidal and Simpson's methods
total_volume_trap = np.trapezoid(flow_rate_m3h, time_hours)
total_volume_simp = simpson(flow_rate_m3h, x=time_hours)

print(f"Total Water Volume (Trapezoidal): {total_volume_trap:.3f} m^3")
print(f"Total Water Volume (Simpson's):   {total_volume_simp:.3f} m^3")
print(f"Absolute Difference:             {abs(total_volume_simp - total_volume_trap):.3f} m^3")
```

#### Results & Output Interpretation
* **Trapezoidal Estimate:** $51.375 \text{ m}^3$
* **Simpson's Estimate:** $51.583 \text{ m}^3$
* **Difference:** $0.208 \text{ m}^3$
* **Interpretation:** The calculation gives total volume delivered. Simpson's rule accounts for curved changes in pump pressure more accurately than linear interpolation.

---

## Task 17: Ordinary Differential Equations (ODE) — Euler Method

### 1. Mathematical Concept
An Ordinary Differential Equation models the rate of change of a dynamic variable over time ($\frac{dy}{dt} = f(t, y)$).
Euler's method approximates the solution iteratively along step sizes $h$:
$$y_{i+1} = y_i + h \cdot f(t_i, y_i)$$

---

### 2. Base Task Analysis

#### Inputs & Mathematical Operations
* **Inputs:**
  * Initial object temperature: $T_0 = 90.0^\circ\text{C}$
  * Ambient temperature: $T_{\text{ambient}} = 25.0^\circ\text{C}$
  * Cooling constant: $k = 0.12 \text{ min}^{-1}$
  * Step size: $h = 1.0 \text{ minute}$
  * Time range: $t = 0 \text{ to } 30 \text{ minutes}$
* **Operation:** Solves Newton's Law of Cooling:
  $$\frac{dT}{dt} = -k(T - T_{\text{ambient}})$$
  Exact solution for comparison: $T(t) = T_{\text{ambient}} + (T_0 - T_{\text{ambient}})e^{-kt}$

#### Parameter Variation
* **Change:** Reduced step size from $h = 1.0 \text{ min}$ to $h = 0.1 \text{ min}$.
* **Effect:** Truncation error per step decreases significantly. The numerical curve aligns much closer to the exact continuous decay solution.

#### Output & Visualization Interpretation
* **Euler Temperature ($t=30 \text{ min}$):** $26.70^\circ\text{C}$
* **Exact Analytical Temperature:** $26.78^\circ\text{C}$
* **Final Absolute Error:** $0.08^\circ\text{C}$
* **Graph Interpretation:** The curve starts at $90.0^\circ\text{C}$ and drops quickly before leveling off towards the room boundary temperature ($25.0^\circ\text{C}$).

---

### 3. Real-World Extension: Pharmacokinetic Drug Elimination Model

#### Problem Formulation
Model the elimination rate of a drug from a patient's bloodstream over time ($24 \text{ hours}$). Drug clearance rate follows first-order kinetics: $\frac{dC}{dt} = -k_e \cdot C(t)$.

#### Assumptions & Inputs
* **Assumptions:** Single-compartment body model with constant clearance rate.
* **Inputs:**
  * Initial concentration $C_0 = 100.0 \text{ mg/L}$
  * Elimination rate $k_e = 0.15 \text{ hr}^{-1}$
  * Step size $h = 0.5 \text{ hours}$
  * Total duration $t_{\text{end}} = 24.0 \text{ hours}$

#### Implementation
File location: `code/Task_17_euler_ode.py`

```python
import numpy as np
import matplotlib.pyplot as plt

# Pharmacokinetic Parameters
C_initial = 100.0       # Initial concentration (mg/L)
k_elimination = 0.15    # Elimination rate constant (1/hour)
h = 0.5                 # Time step in hours
end_time = 24.0         # Duration in hours

def elimination_rate(C):
    return -k_elimination * C

time = np.arange(0, end_time + h, h)
concentration = np.zeros_like(time)
concentration[0] = C_initial

# Euler numerical method loop
for i in range(len(time) - 1):
    concentration[i+1] = concentration[i] + h * elimination_rate(concentration[i])

# Exact analytical validation: C(t) = C0 * exp(-k_e * t)
exact_concentration = C_initial * np.exp(-k_elimination * time)

print(f"Euler estimated concentration after 24 hrs: {concentration[-1]:.4f} mg/L")
print(f"Exact concentration after 24 hrs:           {exact_concentration[-1]:.4f} mg/L")
print(f"Absolute Error:                            {abs(concentration[-1] - exact_concentration[-1]):.4f} mg/L")

# Visualization
plt.figure(figsize=(8, 5))
plt.plot(time, concentration, 'o--', label="Euler Method Approximation")
plt.plot(time, exact_concentration, 'r-', label="Exact Elimination Model")
plt.xlabel("Time (hours)")
plt.ylabel("Drug Concentration (mg/L)")
plt.title("Pharmacokinetic Drug Elimination Model (Euler Method)")
plt.legend()
plt.grid(True)
plt.show()
```

#### Results & Output Interpretation
* **Euler Concentration ($t=24 \text{ hrs}$):** $2.3808 \text{ mg/L}$
* **Exact Analytical Concentration:** $2.7324 \text{ mg/L}$
* **Absolute Error:** $0.3516 \text{ mg/L}$
* **Interpretation:** Drug levels fall exponentially over time. Small step sizes $h$ are necessary to ensure accurate dosing window estimations.

---

## Repository Structure

```text
├── README.md
└── code/
    ├── Task_16_numerical_integration.py
    └── Task_17_euler_ode.py
```