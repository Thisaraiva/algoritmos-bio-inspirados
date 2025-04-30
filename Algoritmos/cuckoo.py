import numpy as np

class CuckooSearch:
    def __init__(self, weights, values, capacity, n_nests=25, iterations=100, pa=0.25, step_size=0.1):
        self.weights = np.array(weights)
        self.values = np.array(values)
        self.capacity = capacity
        self.n_nests = n_nests
        self.iterations = iterations
        self.pa = pa
        self.step_size = step_size
        self.n_items = len(weights)
        
    def initialize_nests(self):
        return np.random.rand(self.n_nests, self.n_items)
    
    def fitness(self, nest):
        solution = self.repair_solution(nest)
        return np.sum(self.values * solution)
    
    def repair_solution(self, nest):
        solution = (nest > 0.5).astype(int)
        total_weight = np.sum(self.weights * solution)
        if total_weight > self.capacity:
            indices = np.where(solution == 1)[0]
            np.random.shuffle(indices)
            for idx in indices:
                if total_weight > self.capacity:
                    solution[idx] = 0
                    total_weight -= self.weights[idx]
        return solution
    
    def levy_flight(self):
        return self.step_size * np.random.randn(self.n_items)
    
    def run(self):
        nests = self.initialize_nests()
        fitnesses = [self.fitness(nest) for nest in nests]
        best_nest = self.repair_solution(nests[np.argmax(fitnesses)]).copy()
        best_fitness = max(fitnesses)
        
        for _ in range(self.iterations):
            for i in range(self.n_nests):
                new_nest = nests[i] + self.levy_flight()
                new_nest = np.clip(new_nest, 0, 1)
                new_fitness = self.fitness(new_nest)
                
                if new_fitness > fitnesses[i]:
                    nests[i] = new_nest
                    fitnesses[i] = new_fitness
            
            for i in range(self.n_nests):
                if np.random.rand() < self.pa:
                    nests[i] = np.random.rand(self.n_items)
                    fitnesses[i] = self.fitness(nests[i])
            
            current_best_idx = np.argmax(fitnesses)
            if fitnesses[current_best_idx] > best_fitness:
                best_fitness = fitnesses[current_best_idx]
                best_nest = self.repair_solution(nests[current_best_idx]).copy()
        
        best_solution = self.repair_solution(best_nest)
        best_fitness = np.sum(self.values * best_solution)
        return best_solution.astype(int), best_fitness