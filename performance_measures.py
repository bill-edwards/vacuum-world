def penalise_dirt(history):

	return sum([len(episode[0].dirty_tiles) for episode in history])
