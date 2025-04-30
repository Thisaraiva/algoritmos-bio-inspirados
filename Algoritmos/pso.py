import numpy as np

class ParticleSwarmOptimization:
    def __init__(self, weights, values, capacity, n_particles=30, iterations=100, w=0.7, c1=1.5, c2=1.5):
        self.weights = np.array(weights)
        self.values = np.array(values)
        self.capacity = capacity
        self.n_particles = n_particles
        self.iterations = iterations
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.n_items = len(weights)
        
    def initialize_particles(self):
        positions = np.random.rand(self.n_particles, self.n_items)
        velocities = np.random.rand(self.n_particles, self.n_items) * 0.1
        return positions, velocities
    
    def fitness(self, position):
        solution = (position > 0.5).astype(int)
        total_weight = np.sum(self.weights * solution)
        if total_weight > self.capacity:
            return 0
        return np.sum(self.values * solution)
    
    def repair_solution(self, position):
        solution = (position > 0.5).astype(int)
        total_weight = np.sum(self.weights * solution)
        if total_weight > self.capacity:
            indices = np.where(solution == 1)[0]
            np.random.shuffle(indices)
            for idx in indices:
                if total_weight > self.capacity:
                    solution[idx] = 0
                    total_weight -= self.weights[idx]
        return solution
    
    def run(self):
        positions, velocities = self.initialize_particles()
        personal_best_positions = positions.copy()
        personal_best_scores = [self.fitness(p) for p in positions]
        global_best_position = personal_best_positions[np.argmax(personal_best_scores)].copy()
        global_best_score = max(personal_best_scores)
        
        for _ in range(self.iterations):
            for i in range(self.n_particles):
                r1, r2 = np.random.rand(), np.random.rand()
                cognitive = self.c1 * r1 * (personal_best_positions[i] - positions[i])
                social = self.c2 * r2 * (global_best_position - positions[i])
                velocities[i] = self.w * velocities[i] + cognitive + social
                
                positions[i] = positions[i] + velocities[i]
                positions[i] = np.clip(positions[i], 0, 1)
                
                repaired_solution = self.repair_solution(positions[i])
                current_fitness = np.sum(self.values * repaired_solution)
                
                if current_fitness > personal_best_scores[i]:
                    personal_best_scores[i] = current_fitness
                    personal_best_positions[i] = repaired_solution.copy()
                    
                    if current_fitness > global_best_score:
                        global_best_score = current_fitness
                        global_best_position = repaired_solution.copy()
        
        best_solution = self.repair_solution(global_best_position)
        best_fitness = np.sum(self.values * best_solution)
        return best_solution.astype(int), best_fitness