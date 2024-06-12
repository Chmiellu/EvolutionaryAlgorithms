import numpy as np
import matplotlib.pyplot as plt

def schwefel(*args):
    return 418.9829 * len(args) - sum(x * np.sin(np.sqrt(abs(x))) for x in args)


if __name__ == "__main__":
    x = np.linspace(-500, 500, 500)
    y = np.linspace(-500, 500, 500)
    X, Y = np.meshgrid(x, y)

    Z = schwefel(X, Y)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Schwefel Function')

    plt.show()