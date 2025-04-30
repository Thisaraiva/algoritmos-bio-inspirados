import numpy as np

class AntColonyOptimization:
    def __init__(self, weights, values, capacity, n_ants=20, iterations=100, alpha=1, beta=2, evaporation=0.5, q0=0.9):
        self.weights = np.array(weights)
        self.values = np.array(values)
        self.capacity = capacity
        self.n_ants = n_ants
        self.iterations = iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation = evaporation
        self.q0 = q0
        self.n_items = len(weights)
        self.heuristic = self.values / self.weights
        self.pheromone = np.ones(self.n_items) / self.n_items
        
    def construct_solution(self):
        solution = np.zeros(self.n_items)
        remaining_capacity = self.capacity
        available_items = list(range(self.n_items))
        
        while available_items:
            probabilities = []
            for item in available_items:
                pheromone = self.pheromone[item] ** self.alpha
                heuristic = self.heuristic[item] ** self.beta
                probabilities.append(pheromone * heuristic)
            
            probabilities = np.array(probabilities)
            if probabilities.sum() == 0:
                probabilities = np.ones(len(probabilities)) / len(probabilities)
            else:
                probabilities /= probabilities.sum()
            
            if np.random.random() < self.q0:
                selected = np.argmax(probabilities)
            else:
                selected = np.random.choice(len(probabilities), p=probabilities)
            
            selected_item = available_items[selected]
            
            if self.weights[selected_item] <= remaining_capacity:
                solution[selected_item] = 1
                remaining_capacity -= self.weights[selected_item]
            
            available_items.pop(selected)
        
        return solution
    
    def update_pheromone(self, solutions, fitnesses):
        self.pheromone *= (1 - self.evaporation)
        for i, fitness in enumerate(fitnesses):
            if fitness > 0:
                self.pheromone += solutions[i] * (fitness / self.capacity)
    
    def run(self):
        best_solution = np.zeros(self.n_items)  # Initialize default solution
        best_fitness = 0
        
        for _ in range(self.iterations):
            solutions = []
            fitnesses = []
            
            for _ in range(self.n_ants):
                solution = self.construct_solution()
                total_weight = np.sum(self.weights * solution)
                fitness = np.sum(self.values * solution) if total_weight <= self.capacity else 0
                solutions.append(solution)
                fitnesses.append(fitness)
                
                if fitness > best_fitness:
                    best_fitness = fitness
                    best_solution = solution.copy()
            
            self.update_pheromone(solutions, fitnesses)
        
        return best_solution.astype(int), best_fitness