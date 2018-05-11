from vacuum_exceptions import InvalidActionError

def standard(old_state, action):

	if (action == 'SUCK'):
		return old_state.clean_tile(old_state.vacuum_location)
	elif (action in ('RIGHT', 'LEFT', 'UP', 'DOWN')):
		return old_state.move_vacuum(action)
	elif (action == 'NONE'):
		return old_state
	else:
		raise InvalidActionError(action)

def slippery(old_state, action):

	if (action == 'SUCK'):
		return old_state.clean_tile(old_state.vacuum_location)
	elif (action in ('RIGHT', 'LEFT', 'UP', 'DOWN')):
		return old_state.move_vacuum(action) if (random.random() < 0.75) else old_state
	elif (action == 'NONE'):
		return old_state
	else:
		raise InvalidActionError(action)