import copy
import random
import numpy as np
from individual import Individual
from FunctionsVisualization.sphere_function import sphere
from FunctionsVisualization.schwefel_function import schwefel
from FunctionsVisualization.dixonprice_function import dixonprice
from FunctionsVisualization.rastrigin_function import rastrigin
from FunctionsVisualization.michalewicz_function import michalewicz

class Population:
    def __init__(self, population_size, is_empty=False):
        self.population_size = population_size
        self.population = []
        if not is_empty:
            for _ in range(population_size):
                individual = Individual()
                self.population.append(individual)
            self.size = len(self.population)

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

    def evaluate(self, fitness_function_name):
        fitness_function = self.get_fitness_function(fitness_function_name)
        for individual in self.population:
            fitness = fitness_function(*individual.genotyp)
            individual.fitness = fitness
        best_individual = min(self.population, key=lambda x: x.fitness)
        self.best_individual = best_individual

    def get_fitness_function(self, name):
        if name == 'schwefel':
            return schwefel
        elif name == 'michalewicz':
            return michalewicz
        elif name == 'rastrigin':
            return rastrigin
        elif name == 'dixonprice':
            return dixonprice
        else:
            return sphere
