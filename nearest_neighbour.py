import pandas as pd
import evaluation
import random
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

# data_points are two 2d array
def nearest_neighbor_tour(data_points):
    # Start from a random location in the data points
    start_index = random.randint(0, len(data_points) - 1)
    current_point = data_points[start_index]

    # Create a KDTree from the data points
    kdtree = KDTree(data_points)

    # List to keep track of visited points
    visited = [False] * len(data_points)
    # Mark the starting index as visited
    visited[start_index] = True

    # To store the order of visited points
    visit_order = [current_point]

    total_distance = 0.0

    # Continue visiting until all points are visited
    while len(visit_order) < len(data_points):
        # Find the nearest neighbor among unvisited points
        distances, indices = kdtree.query(current_point, k=len(data_points))

        # Filter to only consider unvisited points
        unvisited_indices = [i for i in indices if not visited[i]]

        if unvisited_indices:
            # Get the nearest unvisited point
            nearest_index = unvisited_indices[0]
            nearest_point = data_points[nearest_index]

            # Calculate the distance to the nearest point
            distance = np.linalg.norm(current_point - nearest_point)
            total_distance += distance  # Accumulate total distance
            
            # Mark the nearest point as visited
            visited[nearest_index] = True
            
            # Move to the nearest point
            visit_order.append(nearest_point)
            
            # Update the current point
            current_point = nearest_point
        else:
            break

    # Return total distance and the order of visited points
    return total_distance, visit_order