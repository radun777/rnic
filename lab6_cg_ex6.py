import numpy as np
from scipy.spatial import Delaunay

points = np.array([
    [1, 1], [1, -1], [-1, -1], [-1, 1], [0, -2]
])

def calculate_triangulation(lambda_val):
    M = np.array([[0, lambda_val]])
    all_points = np.vstack([points, M])
    tri = Delaunay(all_points)
    edges = set()
    for simplex in tri.simplices:
        for i in range(3):
            edge = tuple(sorted((simplex[i], simplex[(i + 1) % 3])))
            edges.add(edge)
    return len(tri.simplices), len(edges)

lambda_values = np.linspace(-10, 10, 21)
results = [(lmb, *calculate_triangulation(lmb)) for lmb in lambda_values]

for lambda_val, num_triangles, num_edges in results:
    print(f"λ = {lambda_val:.2f}, Triangles = {num_triangles}, Edges = {num_edges}")
