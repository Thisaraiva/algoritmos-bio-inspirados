import random
import numpy as np

class GeneticAlgorithm:
    def __init__(self, weights, values, capacity, population_size=50, generations=100, mutation_rate=0.1):
        self.weights = np.array(weights)
        self.values = np.array(values)
        self.capacity = capacity
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.n_items = len(weights)
        
    def initialize_population(self):
        population = np.zeros((self.population_size, self.n_items), dtype=int)
        for i in range(self.population_size):
            remaining_capacity = self.capacity
            available_items = list(range(self.n_items))
            while available_items and remaining_capacity > 0:
                item = random.choice(available_items)
                if self.weights[item] <= remaining_capacity:
                    population[i, item] = 1
                    remaining_capacity -= self.weights[item]
                available_items.remove(item)
        return population
    
    def fitness(self, individual):
        total_weight = np.sum(self.weights * individual)
        if total_weight > self.capacity:
            return 0
        return np.sum(self.values * individual)
    
    def select_parents(self, population, fitnesses):
        parents = []
        for _ in range(2):
            candidates = np.random.choice(range(len(population)), size=3, replace=False)
            candidates_fitness = [fitnesses[c] for c in candidates]
            parent = population[candidates[np.argmax(candidates_fitness)]]
            parents.append(parent)
        return parents
    
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.n_items-1)
        child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        return child
    
    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual
    
    def run(self):
        population = self.initialize_population()
        best_solution = np.zeros(self.n_items, dtype=int)
        best_fitness = 0
        
        for _ in range(self.generations):
            fitnesses = [self.fitness(ind) for ind in population]
            
            current_best_idx = np.argmax(fitnesses)
            if fitnesses[current_best_idx] > best_fitness:
                best_fitness = fitnesses[current_best_idx]
                best_solution = population[current_best_idx].copy()
            
            new_population = []
            for _ in range(self.population_size // 2):
                parents = self.select_parents(population, fitnesses)
                child1 = self.crossover(parents[0], parents[1])
                child2 = self.crossover(parents[1], parents[0])
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])
            
            population = np.array(new_population)
        
        return best_solution, best_fitness