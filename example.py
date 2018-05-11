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
	pm.penalise_dirt
)

history = te.History(two_tile_floor, agents.TwoTileSimpleReflex(), 5)

print 'Performance score', history.performance_score
