import random
from vacuum_exceptions import UnexpectedPerceptError

# Simple Reflex Agents

class SimpleReflex(object):

	def __init__(self, rules):
		self.rules = rules

	def think(self, percepts):

		for rule in self.rules:
			if rule['condition'](percepts):
				return rule['action']
		else:
			raise UnexpectedPerceptError(percepts)

class StochasticSimpleReflex(object):

	def __init__(self, rules):
		self.rules = rules

	def think(self, percepts):

		random_number = random.random()
		cumulative_probability = 0

		for rule in self.rules:
			if rule['condition'](percepts):
				for action in rule['actions']:
					cumulative_probability += action[0]
					if random_number < cumulative_probability:
						return action[1]
		else:
			raise UnexpectedPerceptError(percepts)

# Model-based Reflex Agents

class ModelBasedReflex(object):

	def __init__(self, model, rules):
		self.model = model
		self.rules = rules

	def think(self, percepts):
		self.model.update_with_percept(percepts)

		for rule in self.rules:
			if rule['condition'](self.model):
				action = rule['action']
				break
		else: action = 'NONE'

		self.model.update_with_action(action)
		return action

# Goal-based Agents

# Generic problem solver (goal-based agent with atomic internal model)
class ProblemSolver(object):

	def __init__(self, problem, search_algorithm, log=False):
		self.problem = problem
		self.search = search_algorithm
		self.plan_formulated = False
		self.log = {} if log else None

	def think(self, percepts):
		if self.log: 'this will be logged'
		if not self.plan_formulated:
			self.action_plan = self.search(self.problem, percepts[0], log=self.log)
			self.plan_formulated = True
		if len(self.action_plan):
			return self.action_plan.pop()
		else:
			return 'NONE'
