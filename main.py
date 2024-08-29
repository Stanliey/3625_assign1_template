import pandas as pd
import evaluation
import time
import numpy as np
import matplotlib.pyplot as plt


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
    tsp = pd.read_csv('./data/10a.csv', index_col=0)
    start_time = time.time()
    route = find_route(tsp)
    elapsed = time.time() - start_time

    # use the provided distance calculation function to measure route distance
    distance = evaluation.measure_distance(tsp, route)
    print(f'found a route with distance {distance:.2f} in {elapsed:.4f}s')

    # plot route
    evaluation.plot_route(tsp, route)
    plt.title(f'distance={distance:.2f}')
    plt.xticks([])
    plt.yticks([])
    plt.show()
