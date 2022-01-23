import numpy as np
import matplotlib.pyplot as plt


class RenderMaze:
	"""A class that will render a holonomy maze"""

	def __init__(self, maze=None):
		self.maze = maze
		self.fig = plt.figure(1)
		self.ax = self.fig.add_subplot(111, projection='3d')

		# Create the unit shpere the maze will be buil on
		u = np.linspace(0, 2 * np.pi, 100)
		v = np.linspace(0, np.pi, 100)
		sx = np.outer(np.cos(u), np.sin(v))
		sy = np.outer(np.sin(u), np.sin(v))
		sz = np.outer(np.ones(np.size(u)), np.cos(v))

		self.sphere = {'x': sx, 'y': sy, 'z': sz}

		# Create the paths that are possible to move along (2 circles)
		cx = np.cos(u)
		cy = np.sin(u)
		cz = np.zeros(shape=u.shape)

		self.paths = {'x': cx, 'y': cy, 'z': cz}

	def render(self):
		"""Render the maze"""
		self.ax.plot_surface(self.sphere['x'], self.sphere['y'], self.sphere['z'], rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)
		self.ax.plot(self.paths['x'], self.paths['y'], self.paths['z'], color='k')
		self.ax.plot(self.paths['z'], self.paths['x'], self.paths['y'], color='k')
		self.ax.plot(self.paths['x'], self.paths['z'], self.paths['y'], color='k')

		plt.axis('off')
		plt.show()
