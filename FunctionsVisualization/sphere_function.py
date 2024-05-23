import numpy as np
import matplotlib.pyplot as plt


def sphere(*args):
    return sum(x ** 2 for x in args)


if __name__ == "__main__":
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = sphere(X, Y)  # Pass X and Y as arguments to sphere_function

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Sphere Function')

    plt.show()
