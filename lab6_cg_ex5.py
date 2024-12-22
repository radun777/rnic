import numpy as np
from scipy.spatial import Delaunay, Voronoi

points_M1 = np.array([
    [0, 0], [1, 0], [0.5, 1], [0.5, -1]
])

points_M2 = np.array([
    [0, 0], [1, 0], [0.5, 1], [0.5, -1], [0.5, 0]
])

tri_M1 = Delaunay(points_M1)
tri_M2 = Delaunay(points_M2)

edges_M1 = set()
edges_M2 = set()

for simplex in tri_M1.simplices:
    for i in range(3):
        edge = tuple(sorted((simplex[i], simplex[(i + 1) % 3])))
        edges_M1.add(edge)

for simplex in tri_M2.simplices:
    for i in range(3):
        edge = tuple(sorted((simplex[i], simplex[(i + 1) % 3])))
        edges_M2.add(edge)

vor_M1 = Voronoi(points_M1)
vor_M2 = Voronoi(points_M2)

half_lines_M1 = sum(1 for region in vor_M1.point_region if -1 in vor_M1.regions[region])
half_lines_M2 = sum(1 for region in vor_M2.point_region if -1 in vor_M2.regions[region])

print(f"M1: {len(points_M1)} points, {len(tri_M1.simplices)} triangles, {len(edges_M1)} edges, {half_lines_M1} half-lines")
print(f"M2: {len(points_M2)} points, {len(tri_M2.simplices)} triangles, {len(edges_M2)} edges, {half_lines_M2} half-lines")
