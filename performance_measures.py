def penalise_dirt(history):

	return sum([len(episode[0].dirty_tiles) for episode in history])

def penalise_dirt_and_movement(history):

	dirt_penalty = sum([len(episode[0].dirty_tiles) for episode in history])
	movement_penalty = 0
	for episode in history:
		if episode[1] in ['RIGHT', 'LEFT']:
			movement_penalty += 1
	return dirt_penalty + movement_penalty