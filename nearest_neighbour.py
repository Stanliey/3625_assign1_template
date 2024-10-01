import pandas as pd
import evaluation
import random
import numpy as np

def find_init_pop(locations: pd.DataFrame) -> list | np.ndarray:

    total_locations = locations.shape[0]
    start_location_index = random.randint (0, total_locations - 1)

    visited = [start_location_index]
    unvisited = locations.drop(start_location_index)
    
    min_distance = float ('inf')
    total_distance = 0

    while not unvisited.empty: #loop until all cities is visited

        for index, _ in unvisited.iterrows():
            
            current = locations.iloc[[visited[-1]]]   # pull current_location info
            target_location = locations.iloc[[index]] # pull taget_location info

            distance = find_distance_bewteen_location(current, target_location)
       
            if distance < min_distance:
                min_distance = distance
                min_index = index

        visited.append(min_index)
        unvisited = unvisited.drop(min_index)
        total_distance = total_distance + min_distance
        min_distance = float ('inf')

    return visited, total_distance

def find_distance_bewteen_location(current_location, target_location):
  
    new_data_strut = pd.concat([current_location, target_location])

    return evaluation.measure_distance(new_data_strut, [0,1])
    
    

