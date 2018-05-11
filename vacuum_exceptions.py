class VacuumWorldError(Exception):
	pass
	
class InvalidActionError(VacuumWorldError):

	def __init__(self, action):
		self.action = action

class UnexpectedPerceptError(VacuumWorldError):

	def __init__(self, percepts):
		self.percepts = percepts

class InvalidStateError(VacuumWorldError):
	pass