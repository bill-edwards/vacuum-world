import random
from vacuum_exceptions import UnexpectedPerceptError

class TwoTileSimpleReflex(object):

	def think(self, percepts):
		dirt_percept, location_percept = percepts

		if (dirt_percept):
			return 'SUCK'
		elif (location_percept == (0,0)):
			return 'RIGHT'
		elif (location_percept == (1,0)):
			return 'LEFT'
		else:
			raise UnexpectedPerceptError(percepts)

class TwoTileModelBasedReflex(object):

	def __init__(self):
		self.cleaned_tiles = set()

	def think(self, percepts):
		dirt_percept, location_percept = percepts

		if (dirt_percept):
			self.cleaned_tiles.add(location_percept)
			return 'SUCK'
		elif (location_percept == (0,0)):
			self.cleaned_tiles.add(location_percept)
			if ((1,0) in self.cleaned_tiles):
				return 'NONE'
			else:
				return 'RIGHT'
		elif (location_percept == (1,0)):
			self.cleaned_tiles.add(location_percept)
			if ((0,0) in self.cleaned_tiles):
				return 'NONE'
			else:
				return 'LEFT'
		else:
			raise UnexpectedPerceptError(percepts)

class Random2DSimpleReflex(object):

	def think(self, percepts):
		dirt_percept, location_percept = percepts

		if (dirt_percept):
			return 'SUCK'
		else:
			random_number = random.random()
			if random_number < 0.25:
				return 'UP'
			elif random_number < 0.5:
				return 'RIGHT'
			elif random_number < 0.75:
				return 'DOWN'
			else: 
				return 'LEFT'