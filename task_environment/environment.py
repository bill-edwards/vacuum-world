import random
from vacuum_exceptions import InvalidStateError, InvalidActionError

class Floor(object):

	def __init__(self, laws, tiles=None, number_of_tiles=20):
		self.laws = laws
		if (tiles == None):
			self.tiles = lay_tiles(number_of_tiles)
		else:
			self.tiles = tiles
		x_coords = [x for (x,y) in self.tiles]
		self.x_min = min(x_coords)
		self.x_max = max(x_coords)
		y_coords = [y for (x,y) in self.tiles]
		self.y_min = min(y_coords)
		self.y_max = max(y_coords)

	# Returns an environment State object.
	def state(self, vacuum_location=None, dirty_tiles=None, dirt_probability=0.5):

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
				elif (direction == 'UP'):
					new_location = (x, y+1)
				elif (direction == 'DOWN'):
					new_location = (x, y-1)
				else:
					new_location = (x, y)
				return self.state(new_location if new_location in self.tiles else state_self.vacuum_location, state_self.dirty_tiles)

			# Cleans a single tile: essentially, removes that tile from the dirty_tiles set.
			def clean_tile(state_self, tile_to_clean):
				return self.state(state_self.vacuum_location, state_self.dirty_tiles - {tile_to_clean})

			# Dirties one or more tiles: essentially adds those tiles to the dirty_tiles set.
			def dirty_tiles(state_self, tiles_to_dirty):
				return self.state(self.vacuum_location, self.dirty_tiles | tiles_to_dirty)

			def stringify(self):
				string_id = str(self.vacuum_location) + '-'
				for tile in sorted(self.dirty_tiles):
					string_id += str(tile)
				return string_id


		if vacuum_location == None:
			vacuum_location = random.sample(self.tiles, 1)[0]

		if (dirty_tiles == None):
			dirty_tiles = set()
			for tile in self.tiles:
				if (random.random() < dirt_probability):
					dirty_tiles.add(tile)

		return State(vacuum_location, dirty_tiles)

	# Evolution law for environment states.
	def tick(self, old_state, action):
		for law in self.laws:
			if action == law['action']:
				if 'state_transform' in law:
					return law['state_transform'](old_state)
				elif 'state_transforms' in law: # Handling non-deterministic laws
					cumulative_probability = 0
					random_number = random.random()
					for transform in law['state_transforms']:
						cumulative_probability += transform[0]
						if random_number < cumulative_probability:
							return transform[1](old_state)
		else:
			return old_state

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

def lay_square_floor(edge_length):
	tiles = set()
	for x in range(edge_length):
		for y in range(edge_length):
			tiles.add((x,y))
	return tiles