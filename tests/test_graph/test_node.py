import numpy as np

from graph.node import Node


def test_node_eq():
	"""Test the equality operator for the node"""
	A = Node(np.ones((3,3)))
	B = Node(np.ones((3,3)))
	C = Node(np.zeros((3,3)))

	assert A == B
	assert A != C
	assert A == np.ones((3,3))
	assert A != np.zeros((3,3))
	assert A != np.ones((4,4))
	assert A in [B, C]
	assert A not in [C, C]