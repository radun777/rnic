import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay

points = np.array([[3, -5], [-6, 6], [6, -4], [5, -5], [9, 10]])

vor = Voronoi(points)

delaunay = Delaunay(points)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
voronoi_plot_2d(vor, show_vertices=False, line_colors='orange', line_width=2)
plt.plot(points[:, 0], points[:, 1], 'bo', label='Points')
plt.title('Voronoi Diagram')
plt.legend()
plt.axis('equal')

plt.subplot(1, 2, 2)
plt.triplot(points[:, 0], points[:, 1], delaunay.simplices, color='orange')
plt.plot(points[:, 0], points[:, 1], 'ro', label='Points')
plt.title('Delaunay Triangulation')
plt.legend()
plt.axis('equal')

plt.tight_layout()
plt.show()
