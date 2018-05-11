class TaskEnvironment(object):

	def __init__(self, environment, state_transition_law, sensors, performance_measure):
		self.environment = environment
		self.state_transition_law = state_transition_law
		self.sensors = sensors
		self.performance_measure = performance_measure

class History(object):

	def __init__(self, task_environment, agent, number_of_steps, initial_state=None):

		state = task_environment.environment.state() if initial_state == None else initial_state
		history = [(state, None)]

		for i in range(number_of_steps):
			print 'STEP', i
			print 'State', state.vacuum_location, state.dirty_tiles
			percepts = [sensor(state) for sensor in task_environment.sensors]
			action = agent.think(percepts)
			print 'Percepts', percepts
			print 'Action', action
			state = task_environment.state_transition_law(state, action)
			history.append((state, action))

		self.performance_score = task_environment.performance_measure(history)