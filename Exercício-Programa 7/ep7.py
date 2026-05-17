import numpy as np
import matplotlib.pyplot as plt

N = [100, 1000, 10000]

for n in N:
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)

    inside = x**2 + y**2 <= 1
    outside = x**2 + y**2 > 1
    #plotando os pontos dentro e fora do círculo
    plt.figure(figsize=(10, 6))
    plt.scatter(x[inside], y[inside], c='blue', s=1, label='Dentro do círculo')
    plt.scatter(x[outside], y[outside], c='red', s=1, label='Fora do círculo')
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Pontos dentro e fora do círculo')
    plt.legend()
    plt.grid(True)
    plt.show()


