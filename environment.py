import random

class Floor(object):

	def __init__(self, tiles=None, number_of_tiles=20):
		if (tiles == None):
			self.tiles = lay_tiles(number_of_tiles)
		else:
			self.tiles = tiles

	def extant_neighbours(self, tile):
		return neighbours(tile) & self.tiles

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

def neighbours(tile):
	x, y = tile
	return {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}

class FloorState(object):

	def __init__(self, floor, vacuum_location=None, dirty_tiles=None, probability_of_dirt=0.25):
		self.floor = floor
		self.tiles = floor.tiles
		self.vacuum_location = random.sample(self.tiles, 1)[0] if vacuum_location == None else vacuum_location
		if (dirty_tiles == None):
			self.dirty_tiles = set()
			for tile in self.tiles:
				if (random.random() < probability_of_dirt):
					self.dirty_tiles.add(tile)
		else:
			self.dirty_tiles = dirty_tiles

	def move_vacuum(self, direction):
		x, y = self.vacuum_location
		if (direction == 'up'):
			new_location = (x, y+1)
		elif (direction == 'down'):
			new_location = (x, y-1)
		elif (direction == 'right'):
			new_location = (x+1, y)
		elif (direction == 'left'):
			new_location = (x-1, y)
		else:
			new_location = (x, y)
		return FloorState(self.floor, new_location if new_location in self.tiles else self.vacuum_location, self.dirty_tiles)

	def dirty_tiles(self, tiles_to_dirty):
		return FloorState(self.floor, self.vacuum_location, self.dirty_tiles | tiles_to_dirty)

	def clean_tile(self, tile_to_clean):
		return FloorState(self.floor, self.vacuum_location, self.dirty_tiles.discard(tile_to_clean))
