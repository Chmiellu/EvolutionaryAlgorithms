import copy
import random
import numpy as np
from individual import Individual
class Population:
    def __init__(self, population_size, is_empty=False):
        self.population_size = population_size
        self.population = []
        if not is_empty:
            for _ in range(population_size):
                individual = Individual()
                self.population.append(individual)
            self.size = len(self.population)


# nieparzyste krzyżowanie
    # def crossover(self, crossover_rate, populationP):
    #     for i, parentP in enumerate(populationP.population):
    #         parentV = self.population[i]
    #         if np.random.random() < crossover_rate:
    #             result_genotyp = np.empty_like(parentV.genotyp)
    #             for j in range(len(parentV.genotyp)):
    #                 if j % 2 == 0:
    #                     result_genotyp[j] = parentV.genotyp[j]
    #                 else:
    #                     result_genotyp[j] = parentP.genotyp[j]
    #             self.population[i].genotyp = result_genotyp

    def crossover(self, crossover_rate, populationP):
        for i, parentP in enumerate(populationP.population):
            parentV = self.population[i]
            for j in range(len(parentV.genotyp)):
                if np.random.random() < crossover_rate:
                    self.population[i].genotyp[j] = parentV.genotyp[j]
                else:
                    self.population[i].genotyp[j] = parentP.genotyp[j]

    def mutate(self, F, population):
        xbest = min(population.population, key=lambda x: x.fitness)
        for individual in population.population:
            selected_individuals = random.sample(population.population, 2)
            xr1, xr2 = [ind.genotyp for ind in selected_individuals]
            vi = xbest.genotyp + F * (xr1 - xr2)
            individual.genotyp = vi

    def succession(self, populationP, populationV):
        for i in range(self.population_size):
            if populationP.population[i].fitness < populationV.population[i].fitness:
                self.population.append(copy.deepcopy(populationP.population[i]))
            else:
                self.population.append(copy.deepcopy(populationV.population[i]))



    def evaluate(self, population):
        self.population = population.population
        for individual in self.population:
            fitness = sum(x ** 2 for x in individual.genotyp)
            individual.fitness = fitness
        best_individual = min(self.population, key=lambda x: x.fitness)
        self.best_individual = best_individual




