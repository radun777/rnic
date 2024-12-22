import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations
import networkx as nx

points = {
    'A': (-1, 6),
    'B': (-1, -1),
    'C': (4, 7),
    'D': (6, 7),
    'E': (1, -1),
    'F': (-5, 3),
    'P': (-2, 3)
}


def point_Q(lambda_val):
    return (2 - lambda_val, 3)


def calculate_mst_length(lambda_val):
    all_points = {**points, 'Q': point_Q(lambda_val)}

    point_coords = list(all_points.values())
    labels = list(all_points.keys())

    dist_matrix = distance_matrix(point_coords, point_coords)

    G = nx.Graph()
    for i, j in combinations(range(len(point_coords)), 2):
        G.add_edge(labels[i], labels[j], weight=dist_matrix[i, j])

    mst = nx.minimum_spanning_tree(G)
    mst_length = sum(data['weight'] for _, _, data in mst.edges(data=True))
    return mst_length


lambda_values = np.linspace(-10, 10, 100)
mst_lengths = [calculate_mst_length(l) for l in lambda_values]

min_index = np.argmin(mst_lengths)
optimal_lambda = lambda_values[min_index]
min_mst_length = mst_lengths[min_index]

optimal_lambda, min_mst_length
