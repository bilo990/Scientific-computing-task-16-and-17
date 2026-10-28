import numpy as np
from scipy.integrate import simpson

# Pipeline flow rate measurements (m^3/hr) over 3 hours (logged every 30 mins)
time_hours = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
flow_rate_m3h = np.array([12.0, 15.5, 20.0, 22.5, 18.0, 14.0, 10.0])

# Compute total volume using Trapezoidal and Simpson's methods
total_volume_trap = np.trapezoid(flow_rate_m3h, time_hours)
total_volume_simp = simpson(flow_rate_m3h, x=time_hours)

print(f"Total Water Volume (Trapezoidal): {total_volume_trap:.3f} m^3")
print(f"Total Water Volume (Simpson's): {total_volume_simp:.3f} m^3")
print(f"Difference: {abs(total_volume_simp - total_volume_trap):.3f} m^3")