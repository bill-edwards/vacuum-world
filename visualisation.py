import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLOUR = (249, 246, 224)
DIRT_COLOUR = (84, 72, 25)
VACUUM_COLOUR = BLACK

WINDOW_MAX_WIDTH = 1000
WINDOW_MAX_HEIGHT = 700
TILE_MAX_SIZE = 100
BORDER = 30
TITLEBAR = 30

def draw_history(floor, history):

	# Adjust window and tile size, depending on dimensions of floor.

	floor_width = (floor.x_max - floor.x_min) + 1
	floor_height = (floor.y_max - floor.y_min) + 1
	floor_max_width = (WINDOW_MAX_WIDTH - (2 * BORDER))/TILE_MAX_SIZE
	floor_max_height = (WINDOW_MAX_HEIGHT - (2 * BORDER) - TITLEBAR)/TILE_MAX_SIZE

	larger_actual_to_max_ratio = max(floor_width/floor_max_width, floor_height/floor_max_height)
	if (larger_actual_to_max_ratio > 1):
		tile_size = TILE_MAX_SIZE/larger_actual_to_max_ratio
	else:
		tile_size = TILE_MAX_SIZE

	window_width = (floor_width * tile_size) + (2 * BORDER)
	window_height = (floor_height * tile_size) + (2 * BORDER + TITLEBAR)
	window_size = (window_width, window_height)

	# Functions for drawing elements of the simulation.

	def draw_tile(tile, colour, offsets):
		x, y = (tile_size * coord - offset for coord, offset in zip(tile, offsets))
		pygame.draw.rect(screen, BLACK, [x, y, tile_size, tile_size])
		pygame.draw.rect(screen, colour, [x+1, y+1, tile_size-2, tile_size-2])

	def draw_vacuum(tile, offsets):
		x, y = ((tile_size * coord) - offset + tile_size/2 for coord, offset in zip(tile, offsets))
		pygame.draw.circle(screen, VACUUM_COLOUR, [x,y], tile_size/3)

	def draw_floor(floor, state, time_step):
		offsets = ((tile_size * floor.x_min) - BORDER, (tile_size * floor.y_min) - BORDER - TITLEBAR)
		for tile in floor.tiles:
			colour = DIRT_COLOUR if tile in state.dirty_tiles else TILE_COLOUR
			draw_tile(tile, colour, offsets)
		draw_vacuum(state.vacuum_location, offsets)
		text = font.render('Step # ' + str(time_step), True, BLACK)
		screen.blit(text, [BORDER, BORDER])

	pygame.init()
	screen = pygame.display.set_mode(window_size)
	pygame.display.set_caption('Vacuum World')
	clock = pygame.time.Clock()
	font = pygame.font.SysFont('Calibri', 20, True, False)

	done = False
	time_step = 1

	while not done:

		clock.tick(2)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: done = True

		screen.fill(WHITE)

		if len(history.history):
			state = history.history.popleft()[0]
			draw_floor(floor, state, time_step)
		else:
			done = True


		time_step += 1
		pygame.display.flip()

	pygame.quit()

