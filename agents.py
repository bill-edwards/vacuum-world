import random
from datetime import datetime
from vacuum_exceptions import UnexpectedPerceptError

# Simple Reflex Agents

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

class SimpleReflex(object):

	def __init__(self, rules):
		self.rules = rules

	def think(self, percepts):

		for rule in self.rules:
			if rule['condition'](percepts):
				return rule['action']

# Model-based Reflex Agents

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

# Goal-based Agents

# Generic problem solver (goal-based agent with atomic internal model)
class ProblemSolver(object):

	def __init__(self, problem, search_algorithm):
		self.problem = problem
		self.search = search_algorithm
		self.plan_formulated = False

	def think(self, percepts):
		if not self.plan_formulated:
			start_time = datetime.now()
			self.action_plan = self.search(self.problem, percepts[0])
			end_time = datetime.now()
			print 'search time: ', end_time - start_time
			self.plan_formulated = True
		if len(self.action_plan):
			return self.action_plan.pop()
		else:
			return 'NONE'
