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