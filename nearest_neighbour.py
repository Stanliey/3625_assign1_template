import pandas as pd
import numpy as np
from scipy.spatial import KDTree
import random

def nearest_neighbor_tour(data_points):
    # Start from a random location in the DataFrame indices
    start_index = random.randint(0, len(data_points) - 1)
    current_point = data_points.iloc[start_index].to_numpy()

    # Create a KDTree from the data points
    kdtree = KDTree(data_points)

    # List to keep track of visited points
    visited = [False] * len(data_points)
    visited[start_index] = True

    # To store the order of visited points' indices
    visit_order_indices = [start_index]

    total_distance = 0.0

    # Continue visiting until all points are visited
    while len(visit_order_indices) < len(data_points):
        # Find the nearest neighbor among unvisited points
        distances, indices = kdtree.query(current_point, k=len(data_points))

        # Filter to only consider unvisited points
        unvisited_indices = [i for i in indices if not visited[i]]

        if unvisited_indices:
            # Get the nearest unvisited point
            nearest_index = unvisited_indices[0]
            nearest_point = data_points.iloc[nearest_index].to_numpy()

            # Calculate the distance to the nearest point
            distance = np.linalg.norm(current_point - nearest_point)
            total_distance += distance  # Accumulate total distance
            
            # Mark the nearest point as visited
            visited[nearest_index] = True
            
            # Move to the nearest point
            print(nearest_index)
            visit_order_indices.append(int(nearest_index))
            
            # Update the current point
            current_point = nearest_point
        else:
            break
    # Return total distance and the order of visited indices
    return visit_order_indices,total_distance