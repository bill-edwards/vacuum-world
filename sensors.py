# Returns a boolean indicating whether or not the tile occupied by the vacuum is dirty.
def dirt_detector(state):
	return state.vacuum_location in state.dirty_tiles

# Returns the tile currently occupied by the vacuum.
def locator(state):
	return state.vacuum_location