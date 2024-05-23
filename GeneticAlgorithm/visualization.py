import numpy as np
from matplotlib import pyplot as plt

def visualize_population(population, fitness_function_name, generation):
    if fitness_function_name == 'sphere':
        visualize_sphere(population, generation)
    elif fitness_function_name == 'michalewicz':
        visualize_michalewicz(population, generation)
    elif fitness_function_name == 'rastrigin':
        visualize_rastrigin(population, generation)
    # Add more visualization functions for other fitness functions as needed

def visualize_sphere(population, generation):
    def sphere(*args):
        return sum(x ** 2 for x in args)

    x = np.linspace(-8, 8, 100)  # Changed the range from -6 to 6 to -8 to 8
    y = np.linspace(-8, 8, 100)  # Changed the range from -6 to 6 to -8 to 8
    X, Y = np.meshgrid(x, y)
    Z = sphere(X, Y)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)

    for individual in population.population:
        ax.scatter(individual.genotyp[0], individual.genotyp[1], individual.fitness, color='red', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Sphere Function')

    ax.text2D(0.05, 0.95, f'Generation: {generation + 1}', transform=ax.transAxes)

    plt.show()
