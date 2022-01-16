import numpy as np


class Node():
	"""A node in a graph"""

	def __init__(self, rep: np.ndarray, connctions: list=None):
		self.rep = rep
		self.connctions = connctions or []

	def connect(self, node):
		"""Connect two nodes"""
		if node not in self.connctions:
			self.connctions.append(node)

	def __eq__(self, other):
		"""Compare the Node to other nodes"""
		if not isinstance(other, (Node, np.ndarray)):
			return False
		if isinstance(other, Node):
			other = other.rep
		if self.rep.shape != other.shape:
			return False
		return np.all(np.all(self.rep == other))
