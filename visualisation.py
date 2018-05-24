import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
TILE_COLOUR = (249, 246, 224)
DIRT_COLOUR = (84, 72, 25)
VACUUM_COLOUR = BLACK

WINDOW_SIZE = (700, 500)

TILE_SIZE = 100

def draw_history(floor, history):

	def draw_tile(tile, colour, offsets):
		x, y = (TILE_SIZE * (coord - offset) + 20 for coord, offset in zip(tile, offsets))
		pygame.draw.rect(screen, BLACK, [x, y, TILE_SIZE, TILE_SIZE])
		pygame.draw.rect(screen, colour, [x+1, y+1, TILE_SIZE-2, TILE_SIZE-2])

	def draw_vacuum(tile, offsets):
		x, y = ((TILE_SIZE * (coord - offset)) + 20 + TILE_SIZE/2 for coord, offset in zip(tile, offsets))
		pygame.draw.circle(screen, VACUUM_COLOUR, [x,y], TILE_SIZE/3)

	def draw_floor(floor, state, time_step):
		offsets = (floor.x_min, floor.y_min)
		for tile in floor.tiles:
			colour = DIRT_COLOUR if tile in state.dirty_tiles else TILE_COLOUR
			draw_tile(tile, colour, offsets)
		draw_vacuum(state.vacuum_location, offsets)
		text = font.render(str(time_step), True, BLUE)
		screen.blit(text, [240, 20])

	pygame.init()
	screen = pygame.display.set_mode(WINDOW_SIZE)
	pygame.display.set_caption('Vacuum World')
	clock = pygame.time.Clock()
	font = pygame.font.SysFont('Calibri', 20, True, False)

	done = False
	time_step = 1

	while not done:

		clock.tick(1)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: done = True

		screen.fill(GREY)

		if len(history.history):
			state = history.history.popleft()[0]
			draw_floor(floor, state, time_step)
		else:
			text = font.render('Performance: ' + str(history.performance_score), True, BLUE)
			screen.blit(text, [20,20])

		time_step += 1
		pygame.display.flip()

	pygame.quit()

