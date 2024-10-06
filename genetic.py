import pandas as pd
import numpy as np
import evaluation
import pygad
import random

def crossover_func (parents, offspring_size, ga_instance):

    #initate size of 2d array
    offspring = np.empty(offspring_size, dtype=parents.dtype)

    row, length = parents.shape

    # run the loop with the number of population 
    for i in range (offspring_size[0]):

        # Generate random numbers of list with the half length as the total locations without duplicates."

        random_indexes_list = np.random.choice(range(length), size = int (length / 2), replace = False)

        # randomly selects which part of route copy to another route
        from_parent = parents[random.randint (0 , row - 1)].copy()
            
        to_parent = parents[random.randint (0 , row - 1)].copy()

        # using the random int from the list
        # to locate which part of indexes that part of to_parent route part 
        # has to have the same location as from_parent route
        # for example; if random_indexes_list have [5, 4, 3, 9, 1]
        # the indexes 5, 4, 3, 9, 1 on to_parent route has to have the same location
        # as the from_parent route. to avoid any location duplicate. swaping is needed
        # before any copying
        for value in random_indexes_list:
            
            # find what location is contain at the index
            from_value_index = np.where(from_parent == value)[0][0]
            
            # save what location is on the index without location duplicate
            temp = to_parent[from_value_index]
            
            # find which index that the saved location have to swap to
            to_value_index = np.where(to_parent == value)[0][0]
            
            # copy the location from the select index from from_parent route have to to_parent route
            to_parent[to_value_index] = temp
            
            # copy the saved location back to_parent
            to_parent[from_value_index] = value
        
        # adds the new route to the new poppulation 
        offspring[i] = to_parent            
         

    return offspring




def run_ga(locations: pd.DataFrame, init_sol):

    def fitness_func(ga_instance, solution, solution_idx):
    
        solution = np.array (solution)
    
        distance = evaluation.measure_distance(locations, solution.astype(int))

        # less distance = higher fitness score
        fitness = 1 / distance * 100
    
        return fitness
    
    # Since the initial_population is passed into the ga_instance, 
    # the GA library sets the population size per solution equal to 
    # the length of the initial population.
    
    ga_instance = pygad.GA(num_generations=100,
                       num_parents_mating=8,
                       fitness_func=fitness_func,
                       num_genes=locations.shape[0],
                       initial_population=init_sol,
                       parent_selection_type='rws',
                       crossover_type=crossover_func,
                       mutation_type='swap',
                       mutation_percent_genes=10)
    
    ga_instance.run()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    
    return solution.astype(int), round(solution_fitness, 2)


