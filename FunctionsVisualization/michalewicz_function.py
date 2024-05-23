import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def michalewicz(*args, m=10):
    n = len(args)
    sum_term = 0
    for i in range(n):
        sum_term += np.sin(args[i]) * (np.sin((i + 1) * args[i] ** 2 / np.pi)) ** (2 * m)
    return -sum_term


if __name__ == "__main__":
    # Create grid of points
    x = np.linspace(0, np.pi, 500)
    y = np.linspace(0, np.pi, 500)
    X, Y = np.meshgrid(x, y)

    # Calculate Z values using the michalewicz function with X and Y as separate arguments
    Z = michalewicz(X, Y)

    # Plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Michalewicz Function')

    plt.show()
