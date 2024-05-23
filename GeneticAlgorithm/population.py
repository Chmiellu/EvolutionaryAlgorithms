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

    def tournament(self, tournament_size, populationP, populationO):
        for _ in range(populationP.population_size):
            selected = random.choices(populationP.population, k=tournament_size)
            winner = min(selected, key=lambda x: x.fitness)
            populationO.population.append(copy.deepcopy(winner))


    def crossover(self, crossover_rate, populationO):
        populationD = Population(population_size=populationO.population_size, is_empty=True)
        for parent_1 in populationO.population:
            if np.random.random() < crossover_rate:
                parent_2 = np.random.choice(populationO.population)
                splitting_point = np.random.randint(1, len(parent_1.genotyp))
                result_genotyp = np.concatenate([
                    parent_1.genotyp[:splitting_point],
                    parent_2.genotyp[splitting_point:]
                ])
                new_one = Individual()
                new_one.genotyp = result_genotyp
                populationD.population.append(new_one)
            else:
                populationD.population.append(parent_1)
        return populationD


    def mutate(self, mutation_rate, populationO):

        for individual in populationO.population:
            if np.random.rand() < mutation_rate:
                if np.random.rand() < 0.5:
                    individual.genotyp *= 0.5
                else:
                    individual.genotyp *= -0.5


    def succession(self, populationP, populationO):
        num_individuals_from_P = int(self.population_size * 0.2)
        num_individuals_from_O = self.population_size - num_individuals_from_P

        sorted_population_P = sorted(populationP.population, key=lambda x: x.fitness)
        sorted_population_O = sorted(populationO.population, key=lambda x: x.fitness)

        selected_individuals = sorted_population_P[:num_individuals_from_P] + sorted_population_O[
                                                                              :num_individuals_from_O]
        populationV = Population(population_size=populationO.population_size, is_empty=True)
        populationV.population = selected_individuals

        return populationV


    def evaluate(self, population, fitness_function_name):
        self.population = population.population
        for individual in self.population:
            genotyp = individual.genotyp
            if fitness_function_name == 'schwefel':
                fitness = schwefel(*genotyp)
            elif fitness_function_name == 'michalewicz':
                fitness = michalewicz(*genotyp)
            elif fitness_function_name == 'rastrigin':
                fitness = rastrigin(*genotyp)
            elif fitness_function_name == 'dixonprice':
                fitness = dixonprice(*genotyp)
            else:
                fitness = sphere(*genotyp)

            individual.fitness = fitness

        best_individual = min(self.population, key=lambda x: x.fitness)
        self.best_individual = best_individual




