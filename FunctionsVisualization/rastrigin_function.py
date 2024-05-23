import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def rastrigin(*args, A=10):
    return A * len(args) + sum(arg ** 2 - A * np.cos(2 * np.pi * arg) for arg in args)


if __name__ == "__main__":
    # Create grid of points
    x = np.linspace(-5.12, 5.12, 500)
    y = np.linspace(-5.12, 5.12, 500)
    X, Y = np.meshgrid(x, y)

    # Calculate Z values using the rastrigin function with X and Y as arguments
    Z = rastrigin(X, Y)

    # Plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Rastrigin Function')

    plt.show()