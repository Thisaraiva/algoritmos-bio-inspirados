from flask import Flask, render_template, request, jsonify
import numpy as np
from Algoritmos.algoritmo_genetico import GeneticAlgorithm
from Algoritmos.aco import AntColonyOptimization
from Algoritmos.pso import ParticleSwarmOptimization
from Algoritmos.cuckoo import CuckooSearch
from Algoritmos.firefly import FireflyAlgorithm

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    weights = data['weights']
    values = data['values']
    capacity = data['capacity']
    algorithm = data['algorithm']
    
    # Convert to integers
    weights = list(map(int, weights))
    values = list(map(int, values))
    capacity = int(capacity)
    
    result = {}
    
    if algorithm == 'ga':
        solver = GeneticAlgorithm(weights, values, capacity)
        solution, fitness = solver.run()
        result = {
            'solution': solution.tolist(),
            'total_value': int(fitness),
            'total_weight': int(np.sum(np.array(weights) * solution))
        }
    elif algorithm == 'aco':
        solver = AntColonyOptimization(weights, values, capacity)
        solution, fitness = solver.run()
        result = {
            'solution': solution.tolist(),
            'total_value': int(fitness),
            'total_weight': int(np.sum(np.array(weights) * solution))
        }
    elif algorithm == 'pso':
        solver = ParticleSwarmOptimization(weights, values, capacity)
        solution, fitness = solver.run()
        result = {
            'solution': solution.tolist(),
            'total_value': int(fitness),
            'total_weight': int(np.sum(np.array(weights) * solution))
        }
    elif algorithm == 'cs':
        solver = CuckooSearch(weights, values, capacity)
        solution, fitness = solver.run()
        result = {
            'solution': solution.tolist(),
            'total_value': int(fitness),
            'total_weight': int(np.sum(np.array(weights) * solution))
        }
    elif algorithm == 'fa':
        solver = FireflyAlgorithm(weights, values, capacity)
        solution, fitness = solver.run()
        result = {
            'solution': solution.tolist(),
            'total_value': int(fitness),
            'total_weight': int(np.sum(np.array(weights) * solution))
        }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)