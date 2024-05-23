import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import TextBox, Slider

def sphere(*args):
    return sum(x ** 2 for x in args)

def dixonprice(*args):
    n = len(args)
    result = (args[0] - 1) ** 2
    for i in range(1, n):
        result += (i + 1) * (2 * args[i] ** 2 - args[i - 1]) ** 2
    return result

def michalewicz(*args, m=10):
    n = len(args)
    sum_term = 0
    for i in range(n):
        sum_term += np.sin(args[i]) * (np.sin((i + 1) * args[i] ** 2 / np.pi)) ** (2 * m)
    return -sum_term

def rastrigin(*args, A=10):
    return A * len(args) + sum(arg ** 2 - A * np.cos(2 * np.pi * arg) for arg in args)

def schwefel(*args):
    return 418.9829 * len(args) - np.sum(np.array(args) * np.sin(np.sqrt(np.abs(np.array(args)))), axis=0)

def visualize_population(population_data, fitness_function_name):
    if fitness_function_name == 'sphere':
        fitness_function = sphere
        x_range = (-8, 8)
        y_range = (-8, 8)
    elif fitness_function_name == 'dixonprice':
        fitness_function = dixonprice
        x_range = (-10, 10)
        y_range = (-10, 10)
    elif fitness_function_name == 'michalewicz':
        fitness_function = michalewicz
        x_range = (0, np.pi)
        y_range = (0, np.pi)
    elif fitness_function_name == 'rastrigin':
        fitness_function = rastrigin
        x_range = (-5.12, 5.12)
        y_range = (-5.12, 5.12)
    elif fitness_function_name == 'schwefel':
        fitness_function = schwefel
        x_range = (-500, 500)
        y_range = (-500, 500)
    else:
        raise ValueError("Unsupported fitness function")

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
