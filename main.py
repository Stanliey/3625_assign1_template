import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
import nearest_neighbour


def find_route(locations: pd.DataFrame) -> list | np.ndarray:
    """
    Function that finds a good route through the provided travelling salesman problem
    :param locations: The x-y coordinates for each location in the TSP. Should be a pandas DataFrame
                        (as returned by pd.read_csv())
    :return: The route through the TSP. Should be a list or array of location indexes, in the desired order.
             The first entry should be the origin city.
             **DO NOT** include the origin city at the end of the list too - the route will be assumed to return to the
             origin city after the list's last entry
    """
    # your code here
    # this function can, of course, make calls to other functions or modules you've written
    # it must return a list of indices defining a route through the TSP

    # note you can convert the DataFrame of x-y coordinates to a 2-d numpy array like this: locations.to_numpy()

    # the following line returns the simple route that visits locations in the order from the data file
    # (replace it with your code)
    return tsp.index


if __name__ == '__main__':

    # here's an example of how to call find_route (and time it)
    tsp = pd.read_csv('./data/250a.csv', index_col=0)

    #firstRow = tsp.iloc[2] # retrieve the row information by row index 
    #value = tsp.loc[1, 'x'] #retrieve the specific value with indexed row

    #tsp = tsp.drop(index = 5)
    #print(tsp.iloc[5])

    #new_tsp = tsp.iloc[[1, 2]].reset_index(drop=True)
    #print(f"the format should be: \n{tsp.iloc[[1, 2]]}\n")
   # route = [0,1]  # From index 1 to 2 to 3 and back to 1
    # Call the measure_distance function

    start_time = time.time()
    init_sol,init_distance = nearest_neighbour.nearest_neighbor_tour(tsp.to_numpy())
    elapsed = time.time() - start_time
    print (f"init_sol: {init_sol}\ninit_distance: {init_distance} in {elapsed}s")
    #total_distance = evaluation.measure_distance(new_tsp, route)
    #print(total_distance)




    #start_time = time.time()
    #route = find_route(tsp)
    #elapsed = time.time() - start_time

    # use the provided distance calculation function to measure route distance
    #distance = evaluation.measure_distance(tsp, route)
    #print(f'found a route with distance {distance:.2f} in {elapsed:.4f}s')

    # plot route
    #evaluation.plot_route(tsp, route)
    #plt.title(f'distance={distance:.2f}')
    # plt.xticks([])
    # plt.yticks([])
    # plt.show()
