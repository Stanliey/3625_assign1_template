import pandas as pd
import numpy as np
import evaluation
import pygad
import random

def crossover_func (parents, offspring_size, ga_instance):

    offspring = np.empty(offspring_size, dtype=parents.dtype)

    row, length = parents.shape

    for i in range (offspring_size[0]):
            
        random_indexes_list = np.random.choice(range(length), size = int (length / 2), replace = False)

        from_parent = parents[random.randint (0 , row - 1)].copy()
            
        to_parent = parents[random.randint (0 , row - 1)].copy()

        for value in random_indexes_list:
            
            from_value_index = np.where(from_parent == value)[0][0]
            
            temp = to_parent[from_value_index]
            
            to_value_index = np.where(to_parent == value)[0][0]
            
            to_parent[to_value_index] = temp
            
            to_parent[from_value_index] = value

        offspring[i] = to_parent            
         

    return offspring




def run_ga(locations: pd.DataFrame, init_sol, mating_num):

    def fitness_func(ga_instance, solution, solution_idx):
    
        solution = np.array (solution)
    
        distance = evaluation.measure_distance(locations, solution.astype(int))
    
        fitness = 1 / distance * 100
    
        return fitness
    
    ga_instance = pygad.GA(num_generations=250,
                       num_parents_mating=mating_num,
                       fitness_func=fitness_func,
                       sol_per_pop=5000,
                       num_genes=locations.shape[0],
                       initial_population=init_sol,
                       parent_selection_type='rws',
                       crossover_type=crossover_func,
                       mutation_type='swap',
                       mutation_percent_genes=10)
    
    ga_instance.run()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    
    return solution.astype(int), round(solution_fitness, 2)


