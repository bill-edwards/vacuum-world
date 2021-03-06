class Problem(object):

	def __init__(self, task_env, goal_test):
		self.env = task_env.environment
		self.pm = task_env.performance_measure
		self.goal_test = goal_test

	def actions(self, state):
		return [law['action'] for law in self.env.laws]

	# Returns the outcome State. Used for planning in deterministic task environments.
	def result(self, state, action):
		return self.env.tick(state, action)

	# Returns an array of possible outcome States. Used for planning in non-deterministic task environments.
	# TO DO: Right now can be duplications if multiple outcomes yield the same state e.g. when succeeding in moving left into a wall, or slipping and failing to move. 
	def results(self, state, action):
		law = [law for law in self.env.laws if law['action'] == action][0]
		if 'state_transform' in law:
			return [law['state_transform'](state)]
		elif 'state_transforms' in law:
			return [transform[1](state) for transform in law['state_transforms']]

	def path_cost(self, state, action):
		episode = (state, action)
		return self.pm(episode)