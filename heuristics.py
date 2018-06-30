def count_dirty_tiles(node):
	# If there are 5 dirty tiles: 5 + 4 + 4 + 3 + 3 + 2 + 2 + 1 + 1
	num_dirty = len(node.state.dirty_tiles)
	return (num_dirty * num_dirty)