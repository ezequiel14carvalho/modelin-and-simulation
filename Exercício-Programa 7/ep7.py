import numpy as np
import matplotlib.pyplot as plt

N = [100, 1000, 10000, 100000, 1000000]
estimates_pi = []
erros = []
true_pi = np.pi

for n in N:
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)

    inside = x**2 + y**2 <= 1
    pi_estimate = 4 * np.mean(inside)
    estimates_pi.append(pi_estimate)
    erros.append(abs(pi_estimate - true_pi))

print("Estimativas de Pi:", estimates_pi)

#plotando as estimativas de Pi
plt.figure(figsize=(10, 6))
plt.plot(N, estimates_pi, marker='o')
plt.axhline(true_pi, color='r', linestyle='--', label='Valor real de Pi')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Número de pontos')
plt.ylabel('Estimativas de Pi')
plt.title('Estimativa de Pi usando o Método de Monte Carlo')
plt.legend()
plt.grid(True)
plt.show()

#plotando as diferênças entre as estimativas e o valor real de Pi
plt.figure(figsize=(10, 6))
plt.plot(N, erros, marker='o')
plt.xscale('log')   
plt.yscale('log')
plt.xlabel('Número de pontos')
plt.ylabel('Erro absoluto')
plt.title('Erro absoluto na estimativa de Pi')
plt.legend()
plt.grid(True)
plt.show()
