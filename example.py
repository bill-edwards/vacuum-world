import task_environment as te
import environment as env
import sensors
import laws
import performance_measures as pm
import agents

two_tile_floor = te.TaskEnvironment(
	env.Floor({(0,0), (1,0)}),
	laws.standard,
	[sensors.dirt_detector, sensors.locator],
	pm.penalise_dirt_and_movement
)

initial_state = two_tile_floor.environment.state()

print '\nSimple Reflex Agent'
history = te.History(two_tile_floor, agents.TwoTileSimpleReflex(), 5, initial_state)
print '\nPerformance score', history.performance_score

print '\nModel-based Reflex Agent'
history = te.History(two_tile_floor, agents.TwoTileModelBasedReflex(), 5, initial_state)
print '\nPerformance score', history.performance_score
