import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import TextBox, Slider
from FunctionsVisualization.sphere_function import sphere
from FunctionsVisualization.schwefel_function import schwefel
from FunctionsVisualization.dixonprice_function import dixonprice
from FunctionsVisualization.rastrigin_function import rastrigin
from FunctionsVisualization.michalewicz_function import michalewicz

def visualize_population(population_data, fitness_function_name):
    fitness_function, x_range, y_range = get_fitness_function_data(fitness_function_name)

    x = np.linspace(*x_range, 100)
    y = np.linspace(*y_range, 100)
    X, Y = np.meshgrid(x, y)
    Z = fitness_function(X, Y)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)

    population = population_data[0]

    for individual in population.population:
        ax.scatter(individual.genotyp[0], individual.genotyp[1], individual.fitness, color='red', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.text2D(0.05, 0.95, f'Visualization for the {fitness_function_name} function', transform=ax.transAxes)

    # Text box for inputting generation
    ax_textbox = plt.axes([0.8, 0.08, 0.1, 0.04])
    textbox = TextBox(ax_textbox, 'Generation', initial='1')

    # Slider for selecting generation
    ax_slider = plt.axes([0.1, 0.02, 0.65, 0.04])
    slider = Slider(ax_slider, 'Generation', 1, len(population_data), valinit=1, valstep=1)

    def submit(text):
        try:
            generation = int(text)
            if 1 <= generation <= len(population_data):
                update(generation)
                slider.set_val(generation)
            else:
                print("Invalid generation number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    textbox.on_submit(submit)

    def update(generation):
        ax.clear()
        ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)
        population = population_data[generation - 1]
        for individual in population.population:
            ax.scatter(individual.genotyp[0], individual.genotyp[1], individual.fitness, color='red', marker='o')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.text2D(0.05, 0.95, f'Visualization for the {fitness_function_name} function', transform=ax.transAxes)

    def update_slider(val):
        generation = int(val)
        update(generation)
        textbox.set_val(str(generation))

    slider.on_changed(update_slider)

    plt.show()

def get_fitness_function_data(name):
    if name == 'schwefel':
        return schwefel, (-500, 500), (-500, 500)
    elif name == 'michalewicz':
        return michalewicz, (0, np.pi), (0, np.pi)
    elif name == 'rastrigin':
        return rastrigin, (-5.12, 5.12), (-5.12, 5.12)
    elif name == 'dixonprice':
        return dixonprice, (-10, 10), (-10, 10)
    else:  # Default is sphere function
        return sphere, (-5.12, 5.12), (-5.12, 5.12)
