import copy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio.v2 as imageio
from io import BytesIO
from population import Population
from parameters import algorithm_parameters


class GeneticAlgorithm:
    def __init__(self, population_size, tournament_size, crossover_rate, mutation_rate, generations):
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations

    def fit(self, fitness_function_name='sphere'):
        populationP = Population(population_size=self.population_size)
        best_genotyp_population = []
        best_genotyp_overall = []
        mean_evaluation_population = []

        images = []
        fig = plt.figure()

        for generation in range(self.generations):
            populationP.evaluate(populationP, fitness_function_name)

            best_individual_population = min(populationP.population, key=lambda x: x.fitness)
            best_genotyp_population.append((best_individual_population.genotyp, best_individual_population.fitness))
            current_best_genotyp = min(populationP.population, key=lambda x: x.fitness)
            if not best_genotyp_overall or min(populationP.population,
                                               key=lambda x: x.fitness).fitness < best_genotyp_overall.fitness:
                best_genotyp_overall = current_best_genotyp
            mean_evaluation_population.append(
                sum(individual.fitness for individual in populationP.population) / self.population_size)

            # Plot and save the population fitness values
            ax = fig.add_subplot(111, projection='3d')
            ax.clear()
            genotypes = np.array([ind.genotyp for ind in populationP.population])
            fitness_values = np.array([ind.fitness for ind in populationP.population])
            ax.scatter(genotypes[:, 0], genotypes[:, 1], fitness_values, c='b', marker='o')
            ax.set_title(f'Generation {generation + 1}')
            ax.set_xlabel('Genotype 1')
            ax.set_ylabel('Genotype 2')
            ax.set_zlabel('Fitness')
            ax.view_init(elev=30, azim=generation * (360 / self.generations))

            # Draw the plot and save to a BytesIO object
            fig.canvas.draw()
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            images.append(imageio.imread(buffer))
            buffer.close()

            populationO = Population(population_size=self.population_size, is_empty=True)
            populationP.tournament(self.tournament_size, populationP, populationO)
            populationD = populationO.crossover(self.crossover_rate, populationO)
            populationO.population = populationD.population
            populationO.mutate(self.mutation_rate, populationO)
            populationO.evaluate(populationO, fitness_function_name)
            populationV = populationO.succession(populationP, populationO)
            populationP = copy.deepcopy(populationV)

        # Save the GIF
        imageio.mimsave('genetic_algorithm_evolution_3d.gif', images, duration=0.5)

        return (
            best_genotyp_population,
            best_genotyp_overall,
            mean_evaluation_population,
        )


genetic_algorithm = GeneticAlgorithm(**algorithm_parameters)
best_genotyp_population, best_genotyp_overall, mean_evaluation_population = genetic_algorithm.fit()

for generation in range(genetic_algorithm.generations):
    print(f"Generation {generation + 1}:")
    print("Best genotyp in population:")
    genotype_rounded = [round(elem, 8) for elem in best_genotyp_population[generation][0]]
    print(f"Genotype: {[f'{elem:.8f}' for elem in genotype_rounded]}")
    print(f"Fitness: {best_genotyp_population[generation][1]:.8f}")
    print(f"Mean evaluation of population: {mean_evaluation_population[generation]::.8f}")
    print()

print("Best genotyp overall:")
genotype_overall_rounded = [round(elem, 8) for elem in best_genotyp_overall.genotyp]
print(f"Genotype: {[f'{elem:.8f}' for elem in genotype_overall_rounded]}")
print(f"Fitness: {best_genotyp_overall.fitness:.8f}")
