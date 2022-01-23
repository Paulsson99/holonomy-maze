from render.render import RenderMaze


def render_maze():
	"""Command line interface for rendering a maze"""
	maze = RenderMaze()
	maze.render()

if __name__ == '__main__':
	render_maze()