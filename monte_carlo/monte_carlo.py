import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return x ** 2

def monte_carlo_simulation(f, a, b, num_points=100000):
    x_range = np.linspace(a, b, 1000)
    y_max = max(f(x_range))

    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, y_max, num_points)

    is_under_curve = y_random < f(x_random)

    rectangle_area = (b - a) * y_max
    integral_mc = rectangle_area * np.sum(is_under_curve) / num_points

    return integral_mc, x_random, y_random, is_under_curve

a_limit = 0
b_limit = 2
num_samples = 15000

mc_result, x_points, y_points, points_under = monte_carlo_simulation(f, a_limit, b_limit, num_samples)
quad_result, error = quad(f, a_limit, b_limit)

print(f"Monte Carlo Result: {mc_result}")
print()
print(f"Quad Function Result: {quad_result}")
print()
print(f"Absolute Difference: {abs(mc_result - quad_result)}")

x_vals = np.linspace(-0.5, 2.5, 400)
plt.figure(figsize=(10, 6))

plt.plot(x_vals, f(x_vals), 'r', label='f(x) = x²', linewidth=2)
plt.fill_between(np.linspace(a_limit, b_limit), f(np.linspace(a_limit, b_limit)), color='gray', alpha=0.2)

plt.scatter(x_points[points_under], y_points[points_under], color='green', s=1, alpha=0.5, label='Points under curve')
plt.scatter(x_points[~points_under], y_points[~points_under], color='blue', s=1, alpha=0.2, label='Points above curve')

plt.axvline(x=a_limit, color='gray', linestyle='--')
plt.axvline(x=b_limit, color='gray', linestyle='--')
plt.title(f'Monte Carlo Integration: S ≈ {mc_result:.4f} (Analytical: {quad_result:.4f})')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()