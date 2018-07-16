def penalise_dirt(episode):

	return len(episode[0].dirty_tiles)

def penalise_dirt_and_movement(episode):

	dirt_penalty = len(episode[0].dirty_tiles)
	movement_penalty = 1 if episode[1] in ['RIGHT', 'LEFT', 'UP', 'DOWN'] else 0
	return dirt_penalty + movement_penalty