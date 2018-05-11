import random
from vacuum_exceptions import InvalidStateError

class Floor(object):

	def __init__(self, tiles=None, number_of_tiles=20):
		if (tiles == None):
			self.tiles = lay_tiles(number_of_tiles)
		else:
			self.tiles = tiles

	def state(self, vacuum_location=None, dirty_tiles=None):

		class State(object):

			def __init__(state_self, vacuum_location, dirty_tiles):
				if (vacuum_location in self.tiles):
					state_self.vacuum_location = vacuum_location
				else:
					raise InvalidStateError('Invalid vacuum_location')
				if (dirty_tiles.issubset(self.tiles)):
					state_self.dirty_tiles = dirty_tiles
				else:
					raise InvalidStateError('Invalid dirty_tiles set')

			# Accepts a direction (up, down, left, right) and moves the vacuum_location to the corresponding new tile, if it exists.
			def move_vacuum(state_self, direction):
				x, y = state_self.vacuum_location
				if (direction == 'RIGHT'):
					new_location = (x+1, y)
				elif (direction == 'LEFT'):
					new_location = (x-1, y)
				else:
					new_location = (x, y)
				return self.state(new_location if new_location in self.tiles else state_self.vacuum_location, state_self.dirty_tiles)

			# Cleans a single tile: essentially, removes that tile from the dirty_tiles set.
			def clean_tile(state_self, tile_to_clean):
				return self.state(state_self.vacuum_location, state_self.dirty_tiles - {tile_to_clean})

			# Dirties one or more tiles: essentially adds those tiles to the dirty_tiles set.
			def dirty_tiles(state_self, tiles_to_dirty):
				return self.state(self.vacuum_location, self.dirty_tiles | tiles_to_dirty)

		if vacuum_location == None:
			vacuum_location = random.sample(self.tiles, 1)[0]

		if (dirty_tiles == None):
			dirty_tiles = set()
			for tile in self.tiles:
				if (random.random() < 0.75):
					dirty_tiles.add(tile)

		return State(vacuum_location, dirty_tiles)


# Utility to create a connected set of tiles of a given number.
# Begins with tile (0,0) and successively adds a tile at a randomly chosen point on the edge of the existing tiles.
def lay_tiles(number_of_tiles):
	current_tile = (0,0)
	tiles = set()
	frontier = set()
	for i in range(number_of_tiles):
		tiles.add(current_tile)
		frontier.discard(current_tile)
		frontier = frontier | (neighbours(current_tile) - tiles)
		current_tile = random.sample(frontier, 1)[0]
	return tiles

# Returns the coordinates of the four spaces surrounding a tile.
# Note - these spaces may not be occupied by existing tiles.
def neighbours(tile):
	x, y = tile
	return {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}
