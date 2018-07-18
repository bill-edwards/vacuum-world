from collections import deque

class TaskEnvironment(object):

	def __init__(self, environment, sensors, performance_measure):
		self.environment = environment
		self.sensors = sensors
		self.performance_measure = performance_measure

class History(object):

	def __init__(self, task_environment, agent, number_of_steps, initial_state=None):

		state = task_environment.environment.state() if initial_state == None else initial_state
		history = deque([(state, None)])

		for i in range(number_of_steps):
			percepts = [sensor(state) for sensor in task_environment.sensors]
			action = agent.think(percepts)
			state = task_environment.environment.tick(state, action)
			history.append((state, action))

		self.history = history
		self.performance_score = sum([task_environment.performance_measure(episode) for episode in history])