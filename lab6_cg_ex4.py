import numpy as np
from scipy.spatial import Voronoi

points_A = [(1 - i, i - 1) for i in range(6)]
points_B = [(i, -i) for i in range(6)]
points_C = [(0, i) for i in range(6)]

points = np.array(points_A + points_B + points_C)

vor = Voronoi(points)

half_lines = 0
for region_index in vor.point_region:
    region = vor.regions[region_index]
    if -1 in region:
        half_lines += 1

print(f"Number of half-lines in the Voronoi diagram: {half_lines}")
