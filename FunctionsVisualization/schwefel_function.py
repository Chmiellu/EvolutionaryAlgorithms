import numpy as np
import matplotlib.pyplot as plt

def schwefel(*args):
    return 418.9829 * len(args) - np.sum(np.array(args) * np.sin(np.sqrt(np.abs(np.array(args)))), axis=0)


if __name__ == "__main__":
    # Create grid of points
    x = np.linspace(-500, 500, 500)
    y = np.linspace(-500, 500, 500)
    X, Y = np.meshgrid(x, y)

    # Calculate Z values using the schwefel function with X and Y as arguments
    Z = schwefel(X, Y)

    # Plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Schwefel Function')

    plt.show()