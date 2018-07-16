class CleanTilesModel(object):

	def __init__(self):
		self.cleaned_tiles = set()
		self.vacuum_location = None

	def update_with_percept(self, percepts):
		dirt_percept, location_percept = percepts
		self.vacuum_location = location_percept
		if (not dirt_percept):
			self.cleaned_tiles.add(self.vacuum_location)

	def update_with_action(self, action):
		if (action == 'SUCK'):
			self.cleaned_tiles.add(self.vacuum_location)