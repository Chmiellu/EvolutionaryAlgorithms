from population import Population
import copy
from parameters import algorithm_parameters
class DifferentialEvolutionAlgorithm:
    def __init__(self, population_size, crossover_rate, mutation_F, generations):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_F = mutation_F
        self.generations = generations

    def fit(self):
        populationP = Population(population_size=self.population_size)

        best_genotyp_population = []
        best_genotyp_overall = []
        mean_evaluation_population = []
        for _ in range(self.generations):
            populationP.evaluate(populationP)

            best_individual_population = min(populationP.population, key=lambda x: x.fitness)
            best_genotyp_population.append((best_individual_population.genotyp, best_individual_population.fitness))
            current_best_genotyp = min(populationP.population, key=lambda x: x.fitness)
            if not best_genotyp_overall  or min(populationP.population,
                                                   key=lambda x: x.fitness).fitness < best_genotyp_overall.fitness:
                best_genotyp_overall = current_best_genotyp
            mean_evaluation_population.append(
                sum(individual.fitness for individual in populationP.population) / self.population_size)

            populationV = copy.deepcopy(populationP)

            populationV.mutate(self.mutation_F, populationV)

            populationV.crossover(self.crossover_rate, populationP)

            populationV.evaluate(populationV)

            populationU = Population(population_size=self.population_size, is_empty=True)

            populationU.succession(populationP, populationV)

            populationP = copy.deepcopy(populationU)


        return (
             best_genotyp_population,
             best_genotyp_overall,
             mean_evaluation_population,
         )


genetic_algorithm = DifferentialEvolutionAlgorithm(**algorithm_parameters)
best_genotyp_population, best_genotyp_overall, mean_evaluation_population = genetic_algorithm.fit()

for generation in range(genetic_algorithm.generations):
    print(f"Generation {generation + 1}:")
    print("Best genotyp in population:")
    genotype_rounded = [round(elem, 8) for elem in best_genotyp_population[generation][0]]
    print(f"Genotype: {[f'{elem:.8f}' for elem in genotype_rounded]}")
    print(f"Fitness: {best_genotyp_population[generation][1]:.8f}")
    print(f"Mean evaluation of population: {mean_evaluation_population[generation]:.8f}")
    print()

print("Best genotyp overall:")
genotype_overall_rounded = [round(elem, 8) for elem in best_genotyp_overall.genotyp]
print(f"Genotype: {[f'{elem:.8f}' for elem in genotype_overall_rounded]}")
print(f"Fitness: {best_genotyp_overall.fitness:.8f}")
