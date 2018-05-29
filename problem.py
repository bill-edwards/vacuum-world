class Problem(object):

	def __init__(self, floor, law):
		self.floor = floor
		self.law = law

	# Returns a list of strings representing actions that will have some observable effect in the given state.
	def actions(self, state):
		actions = []
		if (state.vacuum_location in state.dirty_tiles):
			actions.append('SUCK')
		x, y = state.vacuum_location
		if ((x+1, y) in self.floor.tiles):
			actions.append('RIGHT')
		if ((x-1, y) in self.floor.tiles):
			actions.append('LEFT')
		if ((x, y+1) in self.floor.tiles):
			actions.append('UP')
		if ((x, y-1) in self.floor.tiles):
			actions.append('DOWN')
		return actions

	def result(self, state, action):
		return self.law(state, action)

	def path_cost(self, state, action):
		dirt_cost = len(state.dirty_tiles)
		movement_cost = 1 if action in ['RIGHT', 'LEFT', 'UP', 'DOWN'] else 0
		return dirt_cost + movement_cost

	def goal_test(self, state):
		return True if len(state.dirty_tiles) == 0 else False