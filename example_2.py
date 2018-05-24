import task_environment as te
import environment as env
import sensors
import laws
import performance_measures as pm
import agents
import visualisation

ten_tile_floor = te.TaskEnvironment(
	env.Floor(env.lay_square_floor(4)),
	laws.standard,
	[sensors.dirt_detector, sensors.locator],
	pm.penalise_dirt_and_movement
)

initial_state = ten_tile_floor.environment.state()

print '\nSimple Reflex Agent'
history = te.History(ten_tile_floor, agents.Random2DSimpleReflex(), 100, initial_state)
print '\nPerformance score', history.performance_score

visualisation.draw_history(ten_tile_floor.environment, history)