import numpy as np
import matplotlib.pyplot as plt

N = np.array([100, 1000, 10000])
estimates_pi = []

for n in N:
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)

    inside = x**2 + y**2 <= 1
    pi_estimate = 4 * np.mean(inside)
    estimates_pi.append(pi_estimate)

print("Estimativas de Pi:", estimates_pi)

# CORREÇÃO 1: A ordem correta é fig, ax
plt.figure(figsize=(10, 6))

plt.scatter(x[inside])

# CORREÇÃO 2: Ajustando os nomes dos eixos de acordo com o plot
ax.set_xlabel('N (Número de Pontos)')
ax.set_ylabel('Estimativa de Pi')
ax.set_title('Convergência de Monte Carlo para o valor de Pi')
ax.grid(True)

# CORREÇÃO 3: O show vem do plt
plt.show()