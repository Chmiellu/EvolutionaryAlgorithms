import numpy as np
import matplotlib.pyplot as plt


def dixonprice(*args):
    n = len(args)
    result = (args[0] - 1) ** 2
    for i in range(1, n):
        result += (i + 1) * (2 * args[i] ** 2 - args[i - 1]) ** 2
    return result


if __name__ == "__main__":

    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)

    Z = dixonprice(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Dixon-Price Function')

    plt.show()
