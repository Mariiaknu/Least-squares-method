import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares


def model(params, x):
    a, b = params
    return a * x + b

 # Вектор залишків (помилок)
def residuals(params, x, y):
    return y - model(params, x)


def find_least_sqrt(x, y):
    # приклад лінійної регресії y = a*x + b
    a, b = np.polyfit(x, y, 1)

    # Побудова графіка
    plt.scatter(x, y, label='Дані')
    plt.plot(x, a*x + b, color='red', label=f'Найменші квадрати: y = {a:.2f}x + {b:.2f}')
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Метод найменших квадратів")
    plt.grid(True)
    plt.show()

    return a, b

