import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

points = np.array([
    [5, -1], [7, -1], [9, -1], [7, -3], [11, -1], [-9, 3]
])

points = np.vstack([points, [-15, 0], [15, 0]])

vor = Voronoi(points)

plt.figure(figsize=(8, 8))
voronoi_plot_2d(vor, show_vertices=False, line_colors='orange', line_width=2)
plt.plot(points[:, 0], points[:, 1], 'bo', label='Points')
for i, point in enumerate(points):
    plt.text(point[0], point[1], f"A{i+1}", fontsize=9, color='blue')

plt.title("Voronoi Diagram with 4 Half-line Edges")
plt.axis('equal')
plt.legend()
plt.show()
