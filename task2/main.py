import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi


# Визначення функції для інтегрування
def f(x):
    return x**2


# Візуалізація функції
a, b = 0, 2  # Межі інтегрування
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, "r", linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()


# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integration(f, a, b, samples=100000):
    sum_y = 0
    for _ in range(samples):
        x = random.uniform(a, b)
        sum_y += f(x)
    average_height = sum_y / samples
    area = (b - a) * average_height
    return area


mc_result = monte_carlo_integration(f, a, b, 100000)

# Обчислення інтеграла за допомогою scipy.integrate.quad
quad_result, _ = spi.quad(f, a, b)

print(f"Метод Монте-Карло: {mc_result}, quad: {quad_result}")
