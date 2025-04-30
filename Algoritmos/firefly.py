import numpy as np

class FireflyAlgorithm:
    def __init__(self, weights, values, capacity, n_fireflies=25, iterations=100, alpha=0.2, beta0=1, gamma=1):
        self.weights = np.array(weights)
        self.values = np.array(values)
        self.capacity = capacity
        self.n_fireflies = n_fireflies
        self.iterations = iterations
        self.alpha = alpha
        self.beta0 = beta0
        self.gamma = gamma
        self.n_items = len(weights)
        
    def initialize_fireflies(self):
        return np.random.rand(self.n_fireflies, self.n_items)
    
    def fitness(self, firefly):
        solution = self.repair_solution(firefly)
        return np.sum(self.values * solution)
    
    def repair_solution(self, firefly):
        solution = (firefly > 0.5).astype(int)
        total_weight = np.sum(self.weights * solution)
        if total_weight > self.capacity:
            indices = np.where(solution == 1)[0]
            np.random.shuffle(indices)
            for idx in indices:
                if total_weight > self.capacity:
                    solution[idx] = 0
                    total_weight -= self.weights[idx]
        return solution
    
    def distance(self, a, b):
        return np.sqrt(np.sum((a - b)**2))
    
    def run(self):
        fireflies = self.initialize_fireflies()
        intensities = [self.fitness(f) for f in fireflies]
        best_firefly = self.repair_solution(fireflies[np.argmax(intensities)]).copy()
        best_intensity = max(intensities)
        
        for _ in range(self.iterations):
            for i in range(self.n_fireflies):
                for j in range(self.n_fireflies):
                    if intensities[j] > intensities[i]:
                        r = self.distance(fireflies[i], fireflies[j])
                        beta = self.beta0 * np.exp(-self.gamma * r**2)
                        fireflies[i] += beta * (fireflies[j] - fireflies[i]) + self.alpha * (np.random.rand(self.n_items) - 0.5)
                        fireflies[i] = np.clip(fireflies[i], 0, 1)
                        intensities[i] = self.fitness(fireflies[i])
            
            current_best_idx = np.argmax(intensities)
            if intensities[current_best_idx] > best_intensity:
                best_intensity = intensities[current_best_idx]
                best_firefly = self.repair_solution(fireflies[current_best_idx]).copy()
        
        best_solution = self.repair_solution(best_firefly)
        best_fitness = np.sum(self.values * best_solution)
        return best_solution.astype(int), best_fitness